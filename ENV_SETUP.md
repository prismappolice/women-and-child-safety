# Environment Variables Setup

This application uses environment variables for sensitive configuration data.

## Setup Instructions

### 1. Create .env file in VM

On your production server (VM), create a `.env` file in the project root directory:

```bash
cd ~/women-and-child-safety
nano .env
```

### 2. Add the following configuration

Copy the content from `.env.example` and update with your actual values:

```bash
# Flask Application Configuration
SECRET_KEY=your-secret-key-here
CSRF_SECRET_KEY=your-csrf-secret-key-here

# Database Configuration
DB_NAME=women_safety_db
DB_USER=appuser
DB_PASSWORD=your-actual-database-password
DB_HOST=localhost
DB_PORT=5432

# Email Configuration (Gmail)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=meta1.aihackathon@gmail.com
MAIL_PASSWORD=hgsqrgfhuvqczvaa
ADMIN_EMAIL=meta1.aihackathon@gmail.com

# Application Settings
FLASK_ENV=production
FLASK_DEBUG=False
```

### 3. Generate secure secret keys

You can generate secure random keys using Python:

```bash
python3 -c "import secrets; print(secrets.token_hex(32))"
```

Run this command twice to generate two different keys for `SECRET_KEY` and `CSRF_SECRET_KEY`.

### 4. Set proper file permissions

```bash
chmod 600 .env
```

This ensures only the owner can read/write the file.

### 5. Restart the service

After creating/updating `.env` file:

```bash
sudo systemctl restart women-safety
```

## Important Notes

- ⚠️ **NEVER commit the `.env` file to Git**
- The `.env` file is already in `.gitignore`
- Always use `.env.example` as a template
- Keep your production `.env` file secure and backed up separately
- If you don't create a `.env` file, the application will use default fallback values (for backward compatibility)

## Current Implementation

The application now uses environment variables with fallback to default values:
- `SECRET_KEY` - Flask secret key
- `CSRF_SECRET_KEY` - CSRF protection key
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` - Database credentials
- `MAIL_USERNAME`, `MAIL_PASSWORD` - Email credentials
- `ADMIN_EMAIL` - Admin email address

This means the application will continue to work even without a `.env` file, but using environment variables is highly recommended for production security.
