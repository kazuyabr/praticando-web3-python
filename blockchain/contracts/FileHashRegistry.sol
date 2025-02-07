// SPDX-License-Identifier: MIT
pragma solidity ^0.8.21;

import {AccessControl} from "@openzeppelin/contracts/access/AccessControl.sol";

/**
 * @title FileHashRegistry
 * @dev A contract to register information about files using their hashes.
 */
contract FileHashRegistry is AccessControl {
    /**
     * @dev Throws an error when a file is already registered.
     */
    error FileAlreadyRegistered();

    /**
     * @dev Struct representing a file entry.
     * @param fileName The name of the file.
     * @param fileSize The size of the file in bytes.
     * @param timestamp The timestamp at which the file was registered.
     * @param blockNumber The block number in which the file was registered.
     */
    struct FileEntry {
        bytes32 fileName;
        uint256 fileSize;
        uint256 timestamp;
        uint256 blockNumber;
    }

    /**
     * @dev A counter that keeps track of the number of registered files.
     */
    uint256 public registered;

    /**
     * @dev Mapping from file hashes to file entries.
     */
    mapping(bytes32 => FileEntry) public fileEntries;

    /**
     * @dev Constructor for the contract.
     * Grants the DEFAULT_ADMIN_ROLE to the deployer.
     */
    constructor() {
        _grantRole(DEFAULT_ADMIN_ROLE, msg.sender);
    }

    /**
     * @dev Registers a file hash to the contract.
     * @param fileHash The hash of the file to be registered.
     * @param fileName The name of the file.
     * @param fileSize The size of the file in bytes.
     */
    function registerFileHash(
        bytes32 fileHash,
        bytes32 fileName,
        uint256 fileSize
    ) external onlyRole(DEFAULT_ADMIN_ROLE) {
        if (fileEntries[fileHash].blockNumber != 0) {
            revert FileAlreadyRegistered();
        }

        fileEntries[fileHash] = FileEntry({
            fileName: fileName,
            fileSize: fileSize,
            timestamp: block.timestamp,
            blockNumber: block.number
        });

        registered++;
    }

    /**
     * @dev Returns the file entry for the given file hash.
     * @param fileHash The hash of the file entry to be returned.
     * @return The file entry for the given file hash.
     */
    function getFileEntryByHash(bytes32 fileHash)
        external
        view
        returns (
            bytes32,
            uint256,
            uint256,
            uint256
        )
    {
        FileEntry memory file = fileEntries[fileHash];

        return (file.fileName, file.fileSize, file.timestamp, file.blockNumber);
    }
}