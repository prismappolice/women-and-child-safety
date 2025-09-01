import sqlite3

def fix_district_sp_mapping():
    conn = sqlite3.connect('women_safety.db')
    cursor = conn.cursor()
    
    print("=== FIXING DISTRICT-SP MAPPING ===")
    
    # Step 1: Find Anakapalli district
    cursor.execute('SELECT id, district_name FROM districts WHERE district_name LIKE "%Anakapalli%"')
    anakapalli = cursor.fetchone()
    
    # Step 2: Find Krishna district (where Vijayawada SP should belong)
    cursor.execute('SELECT id, district_name FROM districts WHERE district_name LIKE "%Krishna%"')
    krishna = cursor.fetchone()
    
    if not anakapalli:
        print("Anakapalli district not found!")
        return
    
    if not krishna:
        print("Krishna district not found!")
        return
    
    anakapalli_id, anakapalli_name = anakapalli
    krishna_id, krishna_name = krishna
    
    print(f"Anakapalli District: ID={anakapalli_id}, Name='{anakapalli_name}'")
    print(f"Krishna District: ID={krishna_id}, Name='{krishna_name}'")
    
    # Step 3: Find SP Vijayawada and move it to Krishna district
    cursor.execute('SELECT id, name, district_id FROM district_sps WHERE name LIKE "%Vijayawada%" AND is_active = 1')
    vijayawada_sp = cursor.fetchone()
    
    if vijayawada_sp:
        sp_id, sp_name, current_district_id = vijayawada_sp
        print(f"Found SP: '{sp_name}' currently in district {current_district_id}")
        
        if current_district_id != krishna_id:
            # Move SP Vijayawada to Krishna district
            cursor.execute('UPDATE district_sps SET district_id = ? WHERE id = ?', (krishna_id, sp_id))
            print(f"Moved '{sp_name}' to Krishna district")
    
    # Step 4: Create proper SP for Anakapalli
    cursor.execute('SELECT id FROM district_sps WHERE district_id = ? AND is_active = 1', (anakapalli_id,))
    anakapalli_sps = cursor.fetchall()
    
    if not anakapalli_sps:
        # Add a proper SP for Anakapalli
        cursor.execute('''
            INSERT INTO district_sps (district_id, name, contact_number, email, is_active) 
            VALUES (?, ?, ?, ?, 1)
        ''', (anakapalli_id, 'SP Anakapalli', '+91-8942000000', 'sp.anakapalli@appolice.gov.in'))
        print("Added proper SP for Anakapalli district")
    
    # Step 5: Verify the fix
    print("\n=== VERIFICATION ===")
    cursor.execute('''
        SELECT d.district_name, ds.name 
        FROM districts d 
        JOIN district_sps ds ON d.id = ds.district_id 
        WHERE d.id IN (?, ?) AND ds.is_active = 1
    ''', (anakapalli_id, krishna_id))
    
    mappings = cursor.fetchall()
    for district_name, sp_name in mappings:
        print(f"{district_name} -> {sp_name}")
    
    conn.commit()
    conn.close()
    print("\n=== FIX COMPLETED ===")

if __name__ == "__main__":
    fix_district_sp_mapping()
