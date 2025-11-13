# DocuSign eSign API

[![DocuSign](https://img.shields.io/badge/DocuSign-eSign-orange?logo=docusign)](https://www.docusign.com/)

---

## 1. Initialisation DocuSign eSign

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
