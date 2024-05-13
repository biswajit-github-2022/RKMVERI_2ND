from neo4j import GraphDatabase

class CSVImporter:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Close the connection
        self.driver.close()

    def import_csv(self, file_path):
        with self.driver.session() as session:
            # Cypher query to load CSV and create nodes
            # This is a simple example; customize it as needed
            cypher_query = '''
            LOAD CSV WITH HEADERS FROM $file_path AS row
            CREATE (n:Book {
                post_title: row.`post_title`,
                product_page_url: row.`product_page_url`,
                ebook_Link: row.`ebook Link`,
                audiobook_Link: row.`Audiobook Link`,
                post_excerpt: row.`post_excerpt`,
                sku: row.`sku`,
                regular_price: toFloat(row.`regular_price`),
                sale_price: toFloat(row.`sale_price`),
                weight: toFloat(row.`weight`),
                images: row.`images`,
                meta_total_sales: toInteger(row.`meta:total_sales`),
                tax_product_type: row.`tax:product_type`,
                tax_product_visibility: row.`tax:product_visibility`,
                tax_product_cat: row.`tax:product_cat`,
                tax_product_tag: row.`tax:product_tag`,
                tax_product_shipping_class: row.`tax:product_shipping_class`,
                attribute_Dimension: row.`attribute:Dimension`,
                attribute_Edition: row.`attribute:Edition`,
                attribute_SIZE: row.`attrd 2755 nodibd 2755 nodute:SIZE`,
                attribute_SIZE_Inches: row.`attribute:SIZE (Inches)`,
                attribute_TYPE: row.`attribute:TYPE`,
                attribute_VARIATION: row.`attribute:VARIATION`,
                attribute_pa_artist: row.`attribute:pa_artist`,
                attribute_pa_authorby: row.`attribute:pa_authorby`,
                attribute_pa_binding: row.`attribute:pa_binding`,
                attribute_pa_isbn: row.`attribute:pa_isbn`,
                attribute_pa_language: row.`attribute:pa_language`,
                attribute_pa_media_type: row.`attribute:pa_media-type`,
                attribute_pa_no_of_pages: row.`attribute:pa_no-of-pages`,
                attribute_pa_publisher: row.`attribute:pa_publisher`,
                attribute_pa_subject: row.`attribute:pa_subject`,
                attribute_pa_tags: row.`attribute:pa_tags`
            })
            '''
            # Execute the query
            session.run(cypher_query, file_path=file_path)

# Initialize importer with your Neo4j credentials
importer = CSVImporter("bolt://localhost:7687/", "neo4j", "neo4j123")

# Path to your CSV file
csv_file_path = "file:///books.csv"
# Ensure the file path is accessible by Neo4j, typically by placing the CSV in the import directory of Neo4j

# Import CSV data into Neo4j
importer.import_csv(csv_file_path)

# Close the connection
importer.close()

