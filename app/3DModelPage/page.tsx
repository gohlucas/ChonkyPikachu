"use client"
import React, { useEffect, useState } from 'react';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import * as THREE from 'three';

const ModelPage: React.FC = () => {
  const [selectedModel, setSelectedModel] = useState('/COM1 Basement.glb');

  useEffect(() => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });

    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    const controls = new OrbitControls(camera, renderer.domElement);

    // Ambient light to ensure some light is always present
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.8); 
    scene.add(ambientLight);

    // Directional light for strong illumination
    const directionalLight = new THREE.DirectionalLight(0xffffff, 1.5);
    directionalLight.position.set(10, 10, 10);
    scene.add(directionalLight);

    // Additional point light for extra illumination
    const pointLight = new THREE.PointLight(0xffffff, 1.2, 100);
    pointLight.position.set(10, 10, 10);
    scene.add(pointLight);

    const loader = new GLTFLoader();

    let currentModel: THREE.Group;

    const loadModel = (modelPath: string) => {
      if (currentModel) {
        scene.remove(currentModel);
      }
      loader.load(modelPath, (gltf: THREE.GLTF) => {
        currentModel = gltf.scene;
        currentModel.traverse((node) => {
          if (node.isMesh) {
            node.castShadow = false;
            node.receiveShadow = false;
            // Check for wall objects by name or other criteria
            if (node.name.toLowerCase().includes('wall')) {
              // Scale the wall mesh to make it thicker
              node.scale.set(1.1, 1.1, 1.1); 
            }
          }
        });
        scene.add(gltf.scene);
      });
    };

    loadModel(selectedModel);

    camera.position.set(10, 10, 10); //x,y,z respectively

    const animate = () => {
      requestAnimationFrame(animate);
      controls.update();
      renderer.render(scene, camera);
    };
    animate();

    const handleResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    };

    window.addEventListener('resize', handleResize);

    return () => {
      window.removeEventListener('resize', handleResize);
      document.body.removeChild(renderer.domElement);
    };
  }, [selectedModel]);

  return (
    <div>
      <select onChange={(e) => setSelectedModel(e.target.value)} value={selectedModel}>
        <option value="/COM1 Basement.glb">Basement</option>
        <option value="/COM1 Level 1.glb">First Floor</option>
        <option value="/COM1 Level 2.glb">Second Floor</option>
      </select>
    </div>
  );
};

export default ModelPage;