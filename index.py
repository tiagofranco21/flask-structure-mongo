from app_name.app import initialize_app

app = initialize_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=app.config["PORT"],
            debug=app.config["FLASK_DEBUG"])
