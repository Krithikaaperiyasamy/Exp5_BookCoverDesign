# Ex.05 Book Front Cover Page Design
## Date:20.12.2025

## AIM:
To design a book front cover page using HTML and CSS.

## DESIGN STEPS:

### Step 1:
Create a Django Admin project.

### Step 2:
Create an app in the Django interface.

### Step 3:
Create a folder named 'static' in the app folder.

### Step 4:
Create a new HTML file in the static folder.

### Step 5:
Write the HTML code with relevant CSS properties.

### Step 6:
Choose the appropriate style and color scheme.

### Step 7:
Insert the images in their appropriate places.

### Step 8:
Publish the website in the LocalHost.

## PROGRAM:
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    
	<title>FUNDAMENTALS OF WEB APPLICATION DEVELOPMENT</title>
	<style>
		body{
			background-color:white;
		 	font-family: Arial;
		}
		.cover{
			width: 420px;
			height: 580px;
			background-color:grey;
			border: 3px solid black;
			margin: 50px auto;
			
			padding-top: 30px;
			position: relative; 
			border-radius: 8px;

					}
		.cover img { 	
			text-align: center;
   			width: 300px;
    			margin: 20px auto;
    			display: block;
			border: 2px solid black;
    			border-radius: 8px;
                }
		.title {
			font-size: 20px;
			color:white;
			text-align: center;
		}
		.line {
			text-align:center;
			color: white;
			
		}
		.author {
			font-size: 15px;
			position: absolute;
			width: 130px;  
			height:22px;               
    			               
    			border: 2px solid black;     
   	 		background-color: white;    
    			text-align:center;           
    			left: 280px;               
    			bottom: 20px;             
    			border-radius: 5px;           
    						
                 }                     		
			</style>
</head>
<body>
<div class="cover">
				
		
		<div class="title">
		
		<b>FUNDAMENTALS OF WEB APPLICATION DEVELOPMENT</b>
		</div>
		<img src="{% static 'book_app/cover.png' %}" align="center" >
		
		<div class="line">
		
		<h3><U><i>A Quickstart guide</i></U></h3>

		<ul align="left">

			<li><h5>HTML</h5></li>
			<li><h5>CSS</h5></li>
			<li><h5>JAVA SCRIPT</h5></li>
			<li><h5>BOOT STRAP</h5></li>
		</ul>
		</div>
		
		
		<div class="author">
				
				KRITHIKAA P
		</div>
		
</div>
</body>
</html>
```

## OUTPUT:
![alt text](<Screenshot (29).png>)


## RESULT:
The program for designing book front cover page using HTML and CSS is completed successfully.
