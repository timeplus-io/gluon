
.PHONY: gen 

gen:
	swagger-codegen generate -l python -i ./spec/swagger.yaml -o ./gen --api-package timeplus
	cp -R ./gen/docs/ ./python/docs/
	cp -R ./gen/swagger_client/ ./python/swagger_client/
	cp -R ./gen/test/ ./python/swagger_test/
	rm -rf ./gen