{
    "version": 2,
    "builds": [
      {
        "src": "Todo_App/wsgi.py",
        "use": "@vercel/python"
      }
    ],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "Todo_App/wsgi.py"
      }
    ]
  }
  
