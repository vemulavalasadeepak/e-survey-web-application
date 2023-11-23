<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Advanced Survey</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      background-color: #f2f2f2; /* Light Gray */
      margin: 0;
      padding: 0;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }

    form {
      background-color: #ffffff; /* White */
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
      width: 600px;
      box-sizing: border-box;
    }

    h1 {
      text-align: center;
      color: #3498db; /* Blue */
      text-transform: uppercase;
      letter-spacing: 3px;
      margin-bottom: 20px;
      font-size: 2em;
    }

    h2 {
      color: #555; /* Dark Gray */
      font-size: 1.2em;
      margin-bottom: 10px;
    }

    p {
      margin-bottom: 15px;
      color: #333; /* Black */
    }

    input[type="text"],
    select {
      width: 100%;
      padding: 12px;
      margin-bottom: 15px;
      box-sizing: border-box;
      border: 1px solid #ccc; /* Light Gray */
      border-radius: 6px;
      background-color: #f9f9f9; /* Lighter Gray */
      color: #333; /* Black */
    }

    input[type="submit"] {
      background-color: #27ae60; /* Green */
      color: #fff; /* White */
      padding: 15px 20px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      font-size: 1.2em;
      transition: background-color 0.3s;
    }

    input[type="submit"]:hover {
      background-color: #FFF0F5; /* Darker Green */
    }

    #survey-image {
      width: 100%;
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <form method="post" action="/submit">
    <h1 style="color: #f44336;">Advanced Survey</h1>
    {% for question in questions %}
      <h2>{{ question }}</h2>
      {% if question in options %}
        <select name="{{ question }}" style="background-color: #ffeb3b;">
          {% for option in options[question] %}
            <option value="{{ option }}">{{ option }}</option>
          {% endfor %}
        </select>
      {% else %}
        <input type="text" name="{{ question }}" required style="background-color: #a8ff9f;">
      {% endif %}
      <br>
    {% endfor %}
    <input type="submit" value="Submit" style="background-color: #219653;">
  </form>

  <img id="survey-image" src="download.png" alt="download.png">
</body>
</html>