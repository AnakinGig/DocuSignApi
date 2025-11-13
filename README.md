# DocuSign eSign API

[![DocuSign](https://img.shields.io/badge/DocuSign-eSign-orange?logo=docusign)](https://www.docusign.com/)

---

## 1. Mise à jour de VPS

```bash
sudo apt update && sudo apt upgrade -y
```

## 2. Installation de docker

### Ajouter le repo Docker

```bash
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

### Installer Docker

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
sudo systemctl status docker  # Vérifier le statut
sudo systemctl start docker   # Démarrer si nécessaire
sudo docker run hello-world   # Test rapide
```

## 3. Initialisation DocuSign eSign

1. Créez une application intégrée sur [DocuSign Developer](https://developers.docusign.com/).  
2. Allez dans **My Apps & Keys** -> **Add App and Integration Key**.  
3. Donnez un nom à votre application.
4. Choisissez **Private custom integration**.
5. Dans **Is your application able to securely store a client secret?** cocher **Yes**.
6. Dans **Service Integration**, générez une paire de clés RSA :
   - Copiez la clé publique dans un fichier `public.pem`
   - Copiez la clé privée dans un fichier `private.pem`
7. Dans **Additional settings**, ajoutez une **Redirect URI** :

   ``` bash
   http://localhost:3000/consent-complete
   ```

8. Autorisez la méthode HTTP **POST**.
9. Enregistrez votre application.
