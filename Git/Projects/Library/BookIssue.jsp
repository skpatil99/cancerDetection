<%@page import="java.sql.*"%>

<html>
<head>

<meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>BookIssue</title>

    <!-- Bootstrap -->
    <link href="css/bootstrap.min.css" rel="stylesheet">
	<link rel="stylesheet" href="css/font-awesome.min.css">
	<link rel="stylesheet" href="css/animate.css">
	<link href="css/prettyPhoto.css" rel="stylesheet">
	<link href="css/style.css" rel="stylesheet" />		
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    
    	<!-- Start Styles. Move the 'style' tags and everything between them to between the 'head' tags -->
<style type="text/css">
.myTable { background-color:#FFFFE0;border-collapse:collapse;font-family:Georgia, Garamond, Serif;color:black; }
.myTable th { width:50%;font:bold 18px/1.1em Arial, Helvetica, Sans-Serif;text-shadow: 1px 1px 4px black;letter-spacing:0.3em;background-color:#BDB76B;color:white; }
.myTable td, .myTable th { padding:5px;border:1px solid #BDB76B; }
.myTable td { line-height:2.5em; }

form{
	color:black;
	font-style:italic;
	
}

</style>




</head>

<body>

		<header>		
		<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
			<div class="navigation">
				<div class="container">					
					<div class="navbar-header">
						<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse.collapse">
							<span class="sr-only">Toggle navigation</span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
						</button>
						<div class="navbar-brand">
							<a href="Home.html"><h1><span>Central</span> Library</h1></a>
						</div>
					</div>
					
					<div class="navbar-collapse collapse">							
						<div class="menu">
							<ul class="nav nav-tabs" role="tablist">
								<li role="presentation"><a href="Home.html" class="active">Home</a></li>
								<li role="presentation"><a href="about.html">About Us</a></li>
								<li role="presentation"><a href="login.html">Student</a></li>								
								<li role="presentation"><a href="loginAdmin.jsp">Administrator</a></li>
								<li role="presentation"><a href="contact.html">Contact</a></li>						
							</ul>
						</div>
					</div>						
				</div>
			</div>	
		</nav>		
	</header>
	
	<div id="breadcrumb">
		<div class="container">	
			<div class="breadcrumb">							
				<li><a href="Home.html">Home</a></li>
				<li><a href="loginAdmin.jsp">Admin</a></li>	
				<li>BookIssue</li>		
			</div>		
		</div>	
	</div>
	
	
	<div class="aboutus">
	<div class="container">
			<h3>Insert The Book</h3>
			<hr>
			<div class="col-md-7 wow fadeInDown" data-wow-duration="1000ms" data-wow-delay="300ms">
				<img src="images/7.jpg" class="img-responsive"><br><br>
			</div>
			
			
			<div class="col-md-5 wow fadeInDown" data-wow-duration="1000ms" data-wow-delay="600ms">
				<div class="skill">
					
					<form method="POST" name="form" action="BookIssueOperation.jsp">

						<p>StudentId:</p><input type="text" placeholder="StudentId" name="studentid"><br>
						<p>BookId:</p><input type="text" placeholder="BookId" name="BookId"><br>


						<input type="submit" value="Submit" onclick="window.location.href=BookIssue.jsp">
						<input type="button" value="Home" onclick="window.location.href='Home.html'">

						</form>
					
					

					

					

				</div>	
			</div>
			
			
	</div>
	</div>
	
	<footer>
		<div class="footer">
			<div class="container">
				<div class="social-icon">
					<div class="col-md-4">
						<ul class="social-network">
							<li><a href="#" class="fb tool-tip" title="Facebook"><i class="fa fa-facebook"></i></a></li>
							<li><a href="#" class="twitter tool-tip" title="Twitter"><i class="fa fa-twitter"></i></a></li>
							<li><a href="#" class="gplus tool-tip" title="Google Plus"><i class="fa fa-google-plus"></i></a></li>
							<li><a href="#" class="linkedin tool-tip" title="Linkedin"><i class="fa fa-linkedin"></i></a></li>
							<li><a href="#" class="ytube tool-tip" title="You Tube"><i class="fa fa-youtube-play"></i></a></li>
						</ul>	
					</div>
				</div>
				
				<div class="col-md-4 col-md-offset-4">
					<div class="copyright">
						&copy; June  2015 by <a target="_blank" href="http://bootstraptaste.com/" title="Free Twitter Bootstrap WordPress Themes and HTML templates">Library</a>. All Rights Reserved.
					</div>
                    <!-- 
                        All links in the footer should remain intact. 
                        Licenseing information is available at: http://bootstraptaste.com/license/
                        You can buy this theme without footer links online at: http://bootstraptaste.com/buy/?theme=Company
                    -->
				</div>						
			</div>
			<div class="pull-right">
				<a href="#home" class="scrollup"><i class="fa fa-angle-up fa-3x"></i></a>
			</div>
		</div>
	</footer>
	
   <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
	<script src="js/jquery-2.1.1.min.js"></script>	
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="js/bootstrap.min.js"></script>
	<script src="js/jquery.prettyPhoto.js"></script>
    <script src="js/jquery.isotope.min.js"></script>  
	<script src="js/wow.min.js"></script>
	<script src="js/functions.js"></script>
	






</body>
</html>
