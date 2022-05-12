# Enlaces útiles

- Conexión ssh con putty y archivo ppk: https://www.bluehost.com/help/article/using-ssh-on-windows-putty
- Creación de contraseña de administrador (root) para mysql server: https://exerror.com/failed-error-set-password-has-no-significance-for-user-rootlocalhost-as-the-authentication-method-used-doesnt-store-authentication-data-in-the-mysql-server/ 
- En caso de error 500, esto podría deberse a algún problema en el acceso del servidor web a nuestro proyecto. Algunas opciones para solucionarlo son:
    - Verificar que no haya ningún error en nuestro código (ej. error en la clave del usuario de mysql)
    - Cambiar los permisos de los archivos en nuestro proyecto. 
    
    ```console
        sudo chmod -R 777 2-FlaskMysql/
    ```
    - Agregar el usuario ubuntuo al grupo ```www-data``` para que pueda acceder a los archivos de nuestro proyecto.
    ```console
        sudo usermod -aG www-data ubuntu
    ```