CREATE TABLE IF NOT EXISTS cart(
    id uuid,
    PRIMARY KEY(id)
);
CREATE TABLE IF NOT EXISTS item(
    id uuid,
    cart_id uuid NOT NULL,
    external_id VARCHAR NOT NULL UNIQUE,
    name VARCHAR,
    value INTEGER,
    PRIMARY KEY(id),
    CONSTRAINT fk_cart
      FOREIGN KEY(cart_id)
	  REFERENCES cart(id)
);
ALTER DEFAULT PRIVILEGES IN SCHEMA public
GRANT INSERT, UPDATE, DELETE ON TABLES TO data_tracking
