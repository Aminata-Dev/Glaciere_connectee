<?php
	function connectMaBase(){
		$serveur = "localhost";
			$login = "root";
			$mdp = "";
			$bdd = "temperatures";
			return mysqli_connect($serveur, $login, $mdp, $bdd);
		}
		
	function deconnectMaBase($connexion) {
			mysqli_close($connexion);
		}
?>

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
	<head>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<title>Suivi température glacière</title>
		<link rel="icon" type="image/png" href="icone.png" />
		<link href="style_site.css" rel="stylesheet" media="all" type="text/css">
	</head>
	<body>
		<h1 align=center>Suivi en température de la glacière :</h1><br>
		<div class="table-box">
			<table align="center">
				<tr>
				<th>Horodatage</th>
				<th>Température</th>
				</tr>
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
				//boucle
				while ($data = mysqli_fetch_array($req)) { 
				// on affiche les résultats 

				echo '<tr><td>' . $data['id_horodatage'].' : </td><td>' . $data['temperatures'].' °C</td></tr>';
				}  

				//On libère la mémoire mobilisée pour cette requête dans sql
				//$data de PHP lui est toujours accessible !
				mysqli_free_result ($req);  
				
				// pour se deconnecter
				deconnectMaBase ($connexion);

				?>

			</table>
		</div>
		<footer>
			<a href="http://localhost/phpmyadmin/sql.php?db=temperatures&table=temperatures_glaciere&pos=0" target="_blank"><i>Voir la base de données</i></a><br>
		</footer>
	</body>
</html>
