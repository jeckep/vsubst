## **vsubst** - Simple variables substitution script

Script for performing variables substitution from properties file. 
It can be applied for one file or for directory. It substitutes variable in  **${VAR_NAME}** format.

## Usage

```
python subst.py --props ./example/secure.properties --src_path ./templates --dst_path ./dist
```

## Docker usage

```
docker run --rm  -v "$(pwd):/files"  jeckep/vsubst  --props /files/example/secure.properties --src_path /files/templates --dst_path /files/dist
```

## How to test

```
chmod +x subst.sh
./subst.sh
```
