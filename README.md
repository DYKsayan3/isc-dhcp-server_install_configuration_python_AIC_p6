# isc-dhcp-server_install_configuration_python_AIC_p6
ce code permet l'installation et la configuration du service isc-dhcp-server en python a partir d'un fichier de configuration  json dans un environnement linux (ubuntu 20.04) .
le fichier json sert a sauvegarder les variables de la configuration du service isc-dhcp-server.
Nous avons utilisé visual studio code pour faire du remote code avec l'extension remote ssh sur la machine ubuntu .

Le script vérifie si isc-dhcp-server est installé. Si il est installé alors il est possible de le désinstaller .Si il n'est pas installé, il est possible de l'installer. Le script demandera de choisir l'interface d'ecoute du server dhcp. les adresses: reseau, masque, plage d'adresses, dns, passerelle sont préalablement renseigné dans le fichier json.  le script vous confirme le bon fonctionnement du service.
