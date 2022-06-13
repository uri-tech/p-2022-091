![Alt text](blocks_diagram.png?raw=true "p-2022-091")
client>area low[decrease dbm]->drone->area high->satellite->server

# Stages of communication:
## The "client" initializes a satellite connection.
### 1. "client" sent request to "area low".
### 2. "area low" decrees the p_t(in dBm).
### 3. "area low" send NEW message to the "drone".
### 4. "drone" send the message to "area high".
### 5. "area high" decrees the p_t(in dBm).
### 6. "area high" send the NEW message to the "satellite".
### 1. "satellite" sent new message to "area high".
### 2. "area high" decrees the p_t(in dBm).
### 3. "area high" send NEW message to the "area low".
### 4. "area low" decrees the p_t(in dBm).
### 5. "area low" send the message to the "drone".
### 6. "drone" send the message to the "client".

## Message during connection:
### 1. client sent message to "area low".
### 2. "area low" decrees the p_t(in dBm).
### 3. "area low" send the message to the "drone".
### 4. "drone" Choose whether to drop the package or not.
#### 4.1 "drone" do not drop the package: drone" send the message to "area high".
#### 4.2 "area high" decrees the p_t(in dBm).
#### 4.2 "area high" send the message to the "satellite".