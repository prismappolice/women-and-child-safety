from admin_security import init_admin_security_db, set_security_questions, get_security_questions, verify_security_questions, check_session_timeout

# Initialize admin security database
init_admin_security_db()

@app.route('/admin/setup-security', methods=['GET', 'POST'])
@check_session_timeout
def setup_security_questions():
    if 'admin_logged_in' not in session:
        return redirect(url_for('admin_login'))
        
    if request.method == 'POST':
        # Get the answers from the form
        question1 = request.form.get('question1')
        answer1 = request.form.get('answer1')
        question2 = request.form.get('question2')
        answer2 = request.form.get('answer2')
        question3 = request.form.get('question3')
        answer3 = request.form.get('answer3')
        
        # Validate inputs
        if not all([question1, answer1, question2, answer2, question3, answer3]):
            flash('All questions and answers are required', 'danger')
            return redirect(url_for('setup_security_questions'))
            
        try:
            # Save the security questions
            set_security_questions(question1, answer1, question2, answer2, question3, answer3)
            flash('Security questions have been set successfully', 'success')
            return redirect(url_for('admin_dashboard'))
        except Exception as e:
            flash('An error occurred while saving security questions', 'danger')
            return redirect(url_for('setup_security_questions'))
            
    # For GET request, show the form
    questions = get_security_questions()
    return render_template('setup_security_questions.html', questions=questions)