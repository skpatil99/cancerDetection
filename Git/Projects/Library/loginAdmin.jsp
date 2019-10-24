
<%@page language="java" import="java.sql.*,java.util.*,java.text.*,java.lang.*" %>

<html class="no-js">
<!--<![endif]-->
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<title>STUDENT INFORMATION</title>
<meta name="description" content="">
<meta name="viewport" content="width=device-width">
<link rel="stylesheet" href="css/bootstrap.css">
<link rel="stylesheet" href="css/main.css">


</head>

<body>

<div class="container">
  <div class="row" style="margin-top:20px">
    <div class="col-xs-12 col-sm-8 col-md-6 col-sm-offset-2 col-md-offset-3">
      <form name="form_login" method="post" action="administration.jsp" role="form">
        <fieldset>
          <h2>Please Sign In</h2>
          <hr class="colorgraph">
          <div class="form-group">
            <input name="ID" type="text" id="user_id" class="form-control input-lg" placeholder="Admin Id">
          </div>
          <div class="form-group">
            <input type="password" name="password" id="password" class="form-control input-lg" placeholder="Password">
          </div>
          <hr class="colorgraph">
          <div class="row">
            <div class="col-xs-6 col-sm-6 col-md-6">
					
              <input type="submit" name="Submit" value="Login" class="btn btn-lg btn-success btn-block" onclick="window.location.href='studentInfo.jsp'">
		
		
			

            </div>
            <div class="col-xs-6 col-sm-6 col-md-6">  <input type="button" name="button" value="List of Books" class="btn btn-lg btn-success btn-block" onclick="window.location.href='listofavailablebook.jsp'"></div> 
          </div>
        </fieldset>
      </form>
    </div>
  </div>
</div>






					
					
					
					
					
</body>
</html>
