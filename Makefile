
.PHONY: gen 

gen:
	swagger-codegen generate -l python -i ./spec/swagger.yaml -o ./gen --api-package timeplus
	rm -rf ./python/docs/ && cp -R ./gen/docs/ ./python/docs/
	rm -rf ./python/swagger_client/ && cp -R ./gen/swagger_client/ ./python/swagger_client/
	rm -rf ./python/swagger_test/ && cp -R ./gen/test/ ./python/swagger_test/
	rm -rf ./gen