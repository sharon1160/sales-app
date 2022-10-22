-- Categorías de Unidades de Medida
insert into unit_measure_category (code,name,created_at,updated_at) values
('100','Peso',now(),now()),
('101','Volumen',now(),now()),
('102','Unidades',now(),now());

-- Unidades de Medida
INSERT INTO unit_measure (CODE, NAME,unit_measure_category_id,created_at,updated_at) VALUES
('100','Litro', 2,NOW(),NOW()),
('101','Galonera', 2,NOW(),NOW()),
('102','Kg',1,NOW(),NOW()),
('103','g',1,NOW(),NOW()),
('104','Botella',3,NOW(),NOW()),
('105','Bolsa',1,NOW(),NOW()),
('106','Paquete',3,NOW(),NOW()),
('107','Caja',3,NOW(),NOW());

-- Categorías de Producto
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE table product_category;
SET FOREIGN_KEY_CHECKS = 1;

INSERT INTO product_category (CODE,NAME,percent_discount,created_at,updated_at) VALUES
('100','Bebidas',0, NOW(),NOW()),
('101','Abarrotes',0, NOW(),NOW()),
('102','Frutas',0, NOW(),NOW()),
('103','Aves y Huevos',0, NOW(),NOW()),
('104','Verduras',0, NOW(),NOW()),
('105','Lacteos',0, NOW(),NOW()),
('106','Limpieza',0, NOW(),NOW());

insert into currency(code,symbol,name,created_at,updated_at) values
('PEN', 'S/. ', 'Sol', now(),now()),
('USD', '$. ', 'Dólares Americanos', now(),now());

-- Productos
insert into product (code,name,purchase_price,base_sale_price,percent_discount,discount_amount,sale_price,stock,active,created_at,updated_at,currency_id,product_category_id,unit_measure_id) values
('10000','GASEOSA INCA KOLA BOTELLA 1L', 2.85, 4.70, 5, 0.24, 4.47, 120, 1, now(),now(),1,1,4),
('10001','AZÚCAR RUBIA BOLSA 10KG',23.85, 38.50, 5, 1.93, 36.58, 60, 1,NOW(),NOW(),1,1,4),
('10002','ARROZ RENDIDOR BOLSA 10KG', 31.25, 42.50, 0, 0, 42.50, 75, 1,NOW(),NOW(),1,1,4),
('10003','PALTA FUERTE CAJA 5KG', 36.88, 48.70, 5, 2.43, 46.27, 45, 1,NOW(),NOW(),1,1,4),
('10004','HUEVOS DE GALLINA PAQUETE 15 UN', 5.75, 9.80, 0, 0, 9.80, 90, 1,NOW(),NOW(),1,1,4),
('10005','AGUA MINERAL S/G PAQ. 6 UN 600ML', 4.50, 7.50, 0, 0, 7.50, 120, 1,NOW(),NOW(),1,1,4),
('10006','PAPA BLANCA BOLSA 5KG', 17.25, 26.80, 0, 0, 26.80, 130, 1,NOW(),NOW(),1,1,4),
('10007','ACEITE VEGETAL BOTELLA 900ML', 6.95, 11.18, 5, 0.56, 10.62, 55, 1,NOW(),NOW(),1,1,4),
('10008','LECHE ENTERA PACK 6 UN 1L', 20.88, 32.50, 0, 0, 32.50, 85, 1,NOW(),NOW(),1,1,4),
('10009','LENTEJA BOLSA 1KG', 5.60, 9.30, 0, 0, 9.30, 120, 1,NOW(),NOW(),1,1,4),
('10010','YOGURT FRUTADO BOTELLA 1L', 7.15, 10.70, 5, 0.54, 10.17, 95, 1,NOW(),NOW(),1,1,4),
('10011','QUINUA BOLSA 1KG', 8.25, 13.95, 0, 0, 13.95, 150, 1,NOW(),NOW(),1,1,4),
('10012','LAVAVAJILLAS LIQUIDO LIMON GALONERA 4L', 25.45, 36.85, 15, 5.53, 31.32, 60, 1,NOW(),NOW(),1,1,4),
('10013','LIMPIADOR ANTIGRASA BOTELLA 1L', 23.95, 32.0, 0, 0, 32, 60, 1,NOW(),NOW(),1,1,4),
('10014','TROZOS DE ATUN PAQ. 6 UN LATA 170G', 22.75, 28.95, 10, 2.89, 26.06, 110, 1,NOW(),NOW(),1,1,4),
('10015','PECHUGA ENTERA PAQ. 1KG', 8.50, 15.50, 10, 0.24, 13.95, 60, 1, now(),now(),1,1,7),
('10016','PAPA AMARILLA PERUANITA BOLSA 5KG', 29.90, 43.80, 0, 0.0, 43.80, 70, 1, now(),now(),1,1,6),
('10017','FIDEO SPAGHETTI PAQUETE 1KG', 2.70, 5.60, 0, 0.0, 5.60, 120, 1, now(),now(),1,1,7),
('10018','LECHE EVAPORADA PAQUETE 6 UN 400 ML', 14.50, 23.90, 0, 0.0, 23.90, 120, 1, now(),now(),1,1,7),
('10019','FRESA ENTERA CONGELADA BOLSA 1KG', 7.20, 11.20, 0, 0.0, 11.20, 50, 1, now(),now(),1,1,6),
('10020','PIÑA GOLDEN CONGELADA BOLSA 1KG', 8.90, 15.19, 5, 0.76, 14.43, 50, 1, now(),now(),1,1,6),
('10021','SAL DE MARAS BOLSA 500G', 5.20, 10.55, 0, 0.0, 10.55, 120, 1, now(),now(),1,1,6);

-- Clientes
insert into customer (code, business_name, district, category, ruc, created_at, updated_at) values
('100', 'Cinco Tenedores', 'San Isidro', 'Restaurantes', '20601145852',NOW(),NOW()),
('101', 'Okashi Restaurant', 'Miraflores', 'Restaurantes', '20664585121',NOW(),NOW()),
('102', 'Hotel Palermo', 'San Borja', 'Hoteles', '20365265851', NOW(),NOW()),
('103', 'Mini Market San Blas', 'Surquillo', 'Tiendas', '10426545201', NOW(),NOW()),
('105', 'Supermarket Las Vegas', 'San Borja', 'Tiendas', '20115245110', NOW(),NOW());

-- Pedido
insert into `order` (number, date, delivery_address, delivery_date, subtotal, igv, total, discount_total, created_at, updated_at, customer_id) values
('202200001', '2022-10-05', 'AV. Camino Real 2245 - San Isidro', '2022-10-08', 4548.40, 818.71, 5367.11, 224.00, NOW(), NOW(), 1);

-- Item del pedido
insert into order_item (quantity, total, created_at, updated_at, order_id, product_id) values
(48, 214.56, NOW(), NOW(), 1, 1),
(10, 365.80, NOW(), NOW(), 1, 2),
(15, 637.50, NOW(), NOW(), 1, 3),
(12, 555.24, NOW(), NOW(), 1, 4),
(24, 235.20, NOW(), NOW(), 1, 5),
(15, 112.50, NOW(), NOW(), 1, 6),
(36, 502.20, NOW(), NOW(), 1, 16),
(18, 724.50, NOW(), NOW(), 1, 17),
(24, 643.20, NOW(), NOW(), 1, 7),
(10, 106.20, NOW(), NOW(), 1, 8),
(18, 94.50, NOW(), NOW(), 1, 18),
(12, 357.00, NOW(), NOW(), 1, 9);