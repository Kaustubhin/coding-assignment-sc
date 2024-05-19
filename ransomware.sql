CREATE TABLE ransomwaredata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    iocs TEXT DEFAULT NULL,
    comment TEXT DEFAULT NULL,
    encryptionAlgorithm TEXT DEFAULT NULL,
    snort TEXT DEFAULT NULL,
    extensions TEXT DEFAULT NULL,
    screenshots TEXT DEFAULT NULL,
    microsoftInfo TEXT DEFAULT NULL,
    ransomNoteFilenames TEXT DEFAULT NULL,
    extensionPattern TEXT DEFAULT NULL,
    decryptor TEXT DEFAULT NULL,
    sandbox TEXT DEFAULT NULL,
    microsoftDetectionName TEXT DEFAULT NULL
);


CREATE TABLE resource (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
	resources TEXT
);