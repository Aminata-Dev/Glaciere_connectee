<?php
include("fonctions.php");
?>

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
<head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title>Température glacières</title>
	<link href="style.css" rel="stylesheet" media="all" type="text/css">
</head>
<body>
	<h1 align=center>Voici les températures de notre glacière</h1><br>
	<section>
	
	<?php
	//On se connecte en créant une variable connexion
	$connexion = connectMaBase();
	//message de connexion réussie
	
	//On prépare la requête qui va mettre dans un tableau tout ce qui concerne l’auteur Jando
	$sql = 'SELECT * FROM temperatures_glaciere';  
	// On lance la requête (mysql_query) et on impose un message d'erreur si la requête ne se passe pas (or die) 

	$req = mysqli_query($connexion,$sql) or die('Erreur SQL !<br />'.$sql.'<br />'.mysqli_error($connexion));
	//on organise $req en tableau associatif  $data['champ']
	//en scannant chaque enregistrement récupéré
	//on en profite pour gérer l'affichage
	//titre de la sectionavant la boucle
	echo "<h2>Glacière</h2>";
	//boucle
	while ($data = mysqli_fetch_array($req)) { 
	// on affiche les résultats 
	echo 'Températures à ' .$data['id_horodatage'].' : <strong>'.$data['temperatures'].'</strong>° degrés<br/>';
	}  
	//On libère la mémoire mobilisée pour cette requête dans sql
	//$data de PHP lui est toujours accessible !
	mysqli_free_result ($req);  
	
	// pour se deconnecter
	deconnectMaBase ($connexion);

	?>
	</section>
	<a  href="index.html"><i>Retour INDEX</i></a><br>
</body>
</html>