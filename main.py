import customtkinter as ctk
from PIL import Image
import random
import os
import pyperclip
from data.CTkScrollableDropdown import *

heroes = [{'name': 'Abaddon', 'image': 'abaddon.png'},
          {'name': 'Alchemist', 'image': 'alchemist.png'},
          {'name': 'Ancient Apparition', 'image': 'ancient_apparition.png'},
          {'name': 'Antimage', 'image': 'antimage.png'},
          {'name': 'Arc Warden', 'image': 'arc_warden.png'},
          {'name': 'Axe', 'image': 'axe.png'},
          {'name': 'Bane', 'image': 'bane.png'},
          {'name': 'Batrider', 'image': 'batrider.png'},
          {'name': 'Beastmaster', 'image': 'beastmaster.png'},
          {'name': 'Bloodseeker', 'image': 'bloodseeker.png'},
          {'name': 'Bounty Hunter', 'image': 'bounty_hunter.png'},
          {'name': 'Brewmaster', 'image': 'brewmaster.png'},
          {'name': 'Bristleback', 'image': 'bristleback.png'},
          {'name': 'Broodmother', 'image': 'broodmother.png'},
          {'name': 'Centaur', 'image': 'centaur.png'},
          {'name': 'Chaos Knight', 'image': 'chaos_knight.png'},
          {'name': 'Chen', 'image': 'chen.png'},
          {'name': 'Clinkz', 'image': 'clinkz.png'},
          {'name': 'Clocwerk', 'image': 'rattletrap.png'},
          {'name': 'Crystal Maiden', 'image': 'crystal_maiden.png'},
          {'name': 'Dark Seer', 'image': 'dark_seer.png'},
          {'name': 'Dark Willow', 'image': 'dark_willow.png'},
          {'name': 'Dawnbreaker', 'image': 'dawnbreaker.png'},
          {'name': 'Dazzle', 'image': 'dazzle.png'},
          {'name': 'Death Prophet', 'image': 'death_prophet.png'},
          {'name': 'Disruptor', 'image': 'disruptor.png'},
          {'name': 'Doom Bringer', 'image': 'doom_bringer.png'},
          {'name': 'Dragon Knight', 'image': 'dragon_knight.png'},
          {'name': 'Drow Ranger', 'image': 'drow_ranger.png'},
          {'name': 'Earth Spirit', 'image': 'earth_spirit.png'},
          {'name': 'Earthshaker', 'image': 'earthshaker.png'},
          {'name': 'Elder Titan', 'image': 'elder_titan.png'},
          {'name': 'Ember Spirit', 'image': 'ember_spirit.png'},
          {'name': 'Enchantress', 'image': 'enchantress.png'},
          {'name': 'Enigma', 'image': 'enigma.png'},
          {'name': 'Faceless Void', 'image': 'faceless_void.png'},
          {'name': 'Grimstroke', 'image': 'grimstroke.png'},
          {'name': 'Gyrocopter', 'image': 'gyrocopter.png'},
          {'name': 'Hoodwink', 'image': 'hoodwink.png'},
          {'name': 'Huskar', 'image': 'huskar.png'},
          {'name': 'Invoker', 'image': 'invoker.png'},
          {'name': 'IO', 'image': 'wisp.png'},
          {'name': 'Jakiro', 'image': 'jakiro.png'},
          {'name': 'Juggernaut', 'image': 'juggernaut.png'},
          {'name': 'Keeper Of The Light', 'image': 'keeper_of_the_light.png'},
          {'name': 'Kunkka', 'image': 'kunkka.png'},
          {'name': 'Legion Commander', 'image': 'legion_commander.png'},
          {'name': 'Leshrac', 'image': 'leshrac.png'},
          {'name': 'Lich', 'image': 'lich.png'},
          {'name': 'Life Stealer', 'image': 'life_stealer.png'},
          {'name': 'Lina', 'image': 'lina.png'},
          {'name': 'Lion', 'image': 'lion.png'},
          {'name': 'Lone Druid', 'image': 'lone_druid.png'},
          {'name': 'Luna', 'image': 'luna.png'},
          {'name': 'Lycan', 'image': 'lycan.png'},
          {'name': 'Magnus', 'image': 'magnataur.png'},
          {'name': 'Marci', 'image': 'marci.png'},
          {'name': 'Mars', 'image': 'mars.png'},
          {'name': 'Medusa', 'image': 'medusa.png'},
          {'name': 'Meepo', 'image': 'meepo.png'},
          {'name': 'Mirana', 'image': 'mirana.png'},
          {'name': 'Monkey King', 'image': 'monkey_king.png'},
          {'name': 'Morphling', 'image': 'morphling.png'},
          {'name': 'Muerta', 'image': 'muerta.png'},
          {'name': 'Naga Siren', 'image': 'naga_siren.png'},
          {'name': 'Nature Prophet', 'image': 'furion.png'},
          {'name': 'Necrophos', 'image': 'necrolyte.png'},
          {'name': 'Night Stalker', 'image': 'night_stalker.png'},
          {'name': 'Nyx Assassin', 'image': 'nyx_assassin.png'},
          {'name': 'Obsidian Destroyer', 'image': 'obsidian_destroyer.png'},
          {'name': 'Ogre Magi', 'image': 'ogre_magi.png'},
          {'name': 'Omniknight', 'image': 'omniknight.png'},
          {'name': 'Oracle', 'image': 'oracle.png'},
          {'name': 'Pangolier', 'image': 'pangolier.png'},
          {'name': 'Phantom Assassin', 'image': 'phantom_assassin.png'},
          {'name': 'Phantom Lancer', 'image': 'phantom_lancer.png'},
          {'name': 'Phoenix', 'image': 'phoenix.png'},
          {'name': 'Primal Beast', 'image': 'primal_beast.png'},
          {'name': 'Puck', 'image': 'puck.png'},
          {'name': 'Pudge', 'image': 'pudge.png'},
          {'name': 'Pugna', 'image': 'pugna.png'},
          {'name': 'Queen Of Pain', 'image': 'queenofpain.png'},
          {'name': 'Razor', 'image': 'razor.png'},
          {'name': 'Riki', 'image': 'riki.png'},
          {'name': 'Rubick', 'image': 'rubick.png'},
          {'name': 'Sand King', 'image': 'sand_king.png'},
          {'name': 'Shadowfind', 'image': 'nevermore.png'},
          {'name': 'Shadow Demon', 'image': 'shadow_demon.png'},
          {'name': 'Shadow Shaman', 'image': 'shadow_shaman.png'},
          {'name': 'Silencer', 'image': 'silencer.png'},
          {'name': 'Skywrath Mage', 'image': 'skywrath_mage.png'},
          {'name': 'Slardar', 'image': 'slardar.png'},
          {'name': 'Slark', 'image': 'slark.png'},
          {'name': 'Snapfire', 'image': 'snapfire.png'},
          {'name': 'Sniper', 'image': 'sniper.png'},
          {'name': 'Spectre', 'image': 'spectre.png'},
          {'name': 'Spirit Breaker', 'image': 'spirit_breaker.png'},
          {'name': 'Storm Spirit', 'image': 'storm_spirit.png'},
          {'name': 'Sven', 'image': 'sven.png'},
          {'name': 'Techies', 'image': 'techies.png'},
          {'name': 'Templar Assassin', 'image': 'templar_assassin.png'},
          {'name': 'Terrorblade', 'image': 'terrorblade.png'},
          {'name': 'Tidehunter', 'image': 'tidehunter.png'},
          {'name': 'Timbersaw', 'image': 'shredder.png'},
          {'name': 'Tinker', 'image': 'tinker.png'},
          {'name': 'Tiny', 'image': 'tiny.png'},
          {'name': 'Treant', 'image': 'treant.png'},
          {'name': 'Troll Warlord', 'image': 'troll_warlord.png'},
          {'name': 'Tusk', 'image': 'tusk.png'},
          {'name': 'Undying', 'image': 'undying.png'},
          {'name': 'Underlord', 'image': 'abyssal_underlord.png'},
          {'name': 'Ursa', 'image': 'ursa.png'},
          {'name': 'Vengeful Spirit', 'image': 'vengefulspirit.png'},
          {'name': 'Venomancer', 'image': 'venomancer.png'},
          {'name': 'Viper', 'image': 'viper.png'},
          {'name': 'Visage', 'image': 'visage.png'},
          {'name': 'Void Spirit', 'image': 'void_spirit.png'},
          {'name': 'Warlock', 'image': 'warlock.png'},
          {'name': 'Weaver', 'image': 'weaver.png'},
          {'name': 'Windrunner', 'image': 'windrunner.png'},
          {'name': 'Winter Wyvern', 'image': 'winter_wyvern.png'},
          {'name': 'Witch Doctor', 'image': 'witch_doctor.png'},
          {'name': 'Wraith King', 'image': 'skeleton_king.png'},
          {'name': 'Zeus', 'image': 'zuus.png'}
          ]
items = [
    {'name': 'Abyssal_Blade', 'image': 'Abyssal_Blade.png'},
    {'name': 'Aeon_Disk', 'image': 'Aeon_Disk.png'},
    {'name': 'Aether_Lens', 'image': 'Aether_Lens.png'},
    {'name': 'Ancient_Janggo', 'image': 'Ancient_Janggo.png'},
    {'name': 'Arcane_Blink', 'image': 'Arcane_Blink.png'},
    {'name': 'Arcane_Boots', 'image': 'Arcane_Boots.png'},
    {'name': 'Armlet', 'image': 'Armlet.png'},
    {'name': 'Assault', 'image': 'Assault.png'},
    {'name': 'Basher', 'image': 'Basher.png'},
    {'name': 'Bfury', 'image': 'Bfury.png'},
    {'name': 'Black_King_Bar', 'image': 'Black_King_Bar.png'},
    {'name': 'Blade_Mail', 'image': 'Blade_Mail.png'},
    {'name': 'Blink', 'image': 'Blink.png'},
    {'name': 'Bloodstone', 'image': 'Bloodstone.png'},
    {'name': 'Bloodthorn', 'image': 'Bloodthorn.png'},
    {'name': 'Boots', 'image': 'Boots.png'},
    {'name': 'Butterfly', 'image': 'Butterfly.png'},
    {'name': 'Crimson_Guard', 'image': 'Crimson_Guard.png'},
    {'name': 'Cyclone', 'image': 'Cyclone.png'},
    {'name': 'Dagon_5', 'image': 'Dagon_5.png'},
    {'name': 'Desolator', 'image': 'Desolator.png'},
    {'name': 'Diffusal_Blade', 'image': 'Diffusal_Blade.png'},
    {'name': 'Disperser', 'image': 'Disperser.png'},
    {'name': 'Dragon_Lance', 'image': 'Dragon_Lance.png'},
    {'name': 'Echo_Sabre', 'image': 'Echo_Sabre.png'},
    {'name': 'Eternal_Shroud', 'image': 'Eternal_Shroud.png'},
    {'name': 'Ethereal_Blade', 'image': 'Ethereal_Blade.png'},
    {'name': 'Force_Staff', 'image': 'Force_Staff.png'},
    {'name': 'Gem', 'image': 'Gem.png'},
    {'name': 'Ghost', 'image': 'Ghost.png'},
    {'name': 'Gleipnier', 'image': 'Gleipnier.png'},
    {'name': 'Glimmer_Cape', 'image': 'Glimmer_Cape.png'},
    {'name': 'Grate_Tranquil', 'image': 'Grate_Tranquil.png'},
    {'name': 'Greater_Crit', 'image': 'Greater_Crit.png'},
    {'name': 'Guardian_Greaves', 'image': 'Guardian_Greaves.png'},
    {'name': 'Hand_Of_Midas', 'image': 'Hand_Of_Midas.png'},
    {'name': 'Harpoon', 'image': 'Harpoon.png'},
    {'name': 'Heart', 'image': 'Heart.png'},
    {'name': 'Heavens_Halberd', 'image': 'Heavens_Halberd.png'},
    {'name': 'Helm_Of_The_Dominator', 'image': 'Helm_Of_The_Dominator.png'},
    {'name': 'Helm_Of_The_Overlord', 'image': 'Helm_Of_The_Overlord.png'},
    {'name': 'Holy_Locket', 'image': 'Holy_Locket.png'},
    {'name': 'Hurricane_Pike', 'image': 'Hurricane_Pike.png'},
    {'name': 'Invis_Sword', 'image': 'Invis_Sword.png'},
    {'name': 'Kaya_And_Sange', 'image': 'Kaya_And_Sange.png'},
    {'name': 'Khanda', 'image': 'Khanda.png'},
    {'name': 'Lesser_Crit', 'image': 'Lesser_Crit.png'},
    {'name': 'Lotus_Orb', 'image': 'Lotus_Orb.png'},
    {'name': 'Maelstrom', 'image': 'Maelstrom.png'},
    {'name': 'Mage_Slayer', 'image': 'Mage_Slayer.png'},
    {'name': 'Manta', 'image': 'Manta.png'},
    {'name': 'Mask_Of_Madness', 'image': 'Mask_Of_Madness.png'},
    {'name': 'Mekansm', 'image': 'Mekansm.png'},
    {'name': 'Meteor_Hammer', 'image': 'Meteor_Hammer.png'},
    {'name': 'Mjollnir', 'image': 'Mjollnir.png'},
    {'name': 'Monkey_King_Bar', 'image': 'Monkey_King_Bar.png'},
    {'name': 'Moon_Shard', 'image': 'Moon_Shard.png'},
    {'name': 'Nullifier', 'image': 'Nullifier.png'},
    {'name': 'Octarine_Core', 'image': 'Octarine_Core.png'},
    {'name': 'Orchid', 'image': 'Orchid.png'},
    {'name': 'Overwhelming_Blink', 'image': 'Overwhelming_Blink.png'},
    {'name': 'Parasma', 'image': 'Parasma.png'},
    {'name': 'Phase_Boots', 'image': 'Phase_Boots.png'},
    {'name': 'Phylactery', 'image': 'Phylactery.png'},
    {'name': 'Pipe', 'image': 'Pipe.png'},
    {'name': 'Power_Treads', 'image': 'Power_Treads.png'},
    {'name': 'Radiance', 'image': 'Radiance.png'},
    {'name': 'Rapier', 'image': 'Rapier.png'},
    {'name': 'Refresher', 'image': 'Refresher.png'},
    {'name': 'Revnant_Brooch', 'image': 'Revnant_Brooch.png'},
    {'name': 'Rod_Of_Atos', 'image': 'Rod_Of_Atos.png'},
    {'name': 'Sange_And_Yasha', 'image': 'Sange_And_Yasha.png'},
    {'name': 'Satanic', 'image': 'Satanic.png'},
    {'name': 'Sheepstick', 'image': 'Sheepstick.png'},
    {'name': 'Shivas_Guard', 'image': 'Shivas_Guard.png'},
    {'name': 'Silver_Edge', 'image': 'Silver_Edge.png'},
    {'name': 'Skadi', 'image': 'Skadi.png'},
    {'name': 'Solar_Crest', 'image': 'Solar_Crest.png'},
    {'name': 'Sphere', 'image': 'Sphere.png'},
    {'name': 'Spirit_Vessel', 'image': 'Spirit_Vessel.png'},
    {'name': 'Swigt_Blink', 'image': 'Swigt_Blink.png'},
    {'name': 'Tranquil_Boots', 'image': 'Tranquil_Boots.png'},
    {'name': 'Travel_Boots', 'image': 'Travel_Boots.png'},
    {'name': 'Travel_Boots_2', 'image': 'Travel_Boots_2.png'},
    {'name': 'Ultimate_Scepter', 'image': 'Ultimate_Scepter.png'},
    {'name': 'Urn_Of_Shadows', 'image': 'Urn_Of_Shadows.png'},
    {'name': 'Vanguard', 'image': 'Vanguard.png'},
    {'name': 'Veil_Of_Discord', 'image': 'Veil_Of_Discord.png'},
    {'name': 'Vladmir', 'image': 'Vladmir.png'},
    {'name': 'Wind_Waker', 'image': 'Wind_Waker.png'},
    {'name': 'Witch_Blade', 'image': 'Witch_Blade.png'},
    {'name': 'Yasha_And_Kaya', 'image': 'Yasha_And_Kaya.png'}
]
talants = [{'name': 'Screenshot_0', 'image': 'Screenshot_0.png'},
           {'name': 'Screenshot_1', 'image': 'Screenshot_1.png'},
           {'name': 'Screenshot_2', 'image': 'Screenshot_2.png'},
           {'name': 'Screenshot_3', 'image': 'Screenshot_3.png'},
           {'name': 'Screenshot_4', 'image': 'Screenshot_4.png'},
           {'name': 'Screenshot_5', 'image': 'Screenshot_5.png'},
           {'name': 'Screenshot_6', 'image': 'Screenshot_6.png'},
           {'name': 'Screenshot_7', 'image': 'Screenshot_7.png'},
           {'name': 'Screenshot_8', 'image': 'Screenshot_8.png'},
           {'name': 'Screenshot_9', 'image': 'Screenshot_9.png'},
           {'name': 'Screenshot_10', 'image': 'Screenshot_10.png'},
           {'name': 'Screenshot_11', 'image': 'Screenshot_11.png'},
           {'name': 'Screenshot_12', 'image': 'Screenshot_12.png'},
           {'name': 'Screenshot_13', 'image': 'Screenshot_13.png'},
           {'name': 'Screenshot_14', 'image': 'Screenshot_14.png'},
           {'name': 'Screenshot_15', 'image': 'Screenshot_15.png'},
           ]
sapogi = [
    {'name': 'Phase_Boots', 'image': 'Phase_Boots.png'},
    {'name': 'Tranquil_Boots', 'image': 'Tranquil_Boots.png'},
    {'name': 'Travel_Boots', 'image': 'Travel_Boots.png'},
    {'name': 'Travel_Boots_2', 'image': 'Travel_Boots_2.png'},
    {'name': 'Power_Treads', 'image': 'Power_Treads.png'},
    {'name': 'Boots', 'image': 'Boots.png'},
    {'name': 'Guardian_Greaves', 'image': 'Guardian_Greaves.png'},
    {'name': 'Grate_Tranquil', 'image': 'Grate_Tranquil.png'},
    {'name': 'Arcane_Boots', 'image': 'Arcane_Boots.png'},
]

selected_hero = None
selected_items = []
selected_talant = None


class GenerateNick:

    def __init__(self):
        self.ghoul_count = 0
        self.ghoul_count_need = random.randint(3, 6)
        self.symbols = list(
            "彡༒☬☠️♕彡༒☬☠️♕乡☬牡マキグ⛥⛥⛥⛥⛥ナルファマキグナルファ系路克瑞大阪市立学鎰命科ャマ能力ϒ人は妻スティ要通り玉宏¥サ丹谷Ѫ灯影伝鶐能力ϒ人は妻スティ私はディックを吸う六怒り"
        )
        self.aor = ["", "or feed", "or leave", "or afk", "or suicide",
                    "или пудж с момкой", "или фид", "или лес", "or jungle"]
        self.sfix = [
            lambda: "zxc" * random.randint(1, 4),
            lambda: "zxc" * random.randint(1, 4),
            lambda: f'{random.randint(0, 6)}-{random.randint(0, 6)} pos {random.choice(self.aor)}',
            lambda: f'{random.randint(0, 10)}к узник',
            lambda: "dead inside",
            lambda: "dead inside",
            lambda: "dead outside",
            lambda: self.warp_symbols("дед внутри", 0, 2),
            lambda: "clown",
            lambda: self.warp_symbols("rotting", 0, 2),
            lambda: self.warp_symbols("мёртв", 0, 2),
            lambda: "мёртв внутри",
            lambda: self.warp_symbols("anti social", 0, 2),
            lambda: "anti social",
            lambda: "crying",
            lambda: self.warp_symbols("eternal despair", 0, 2),
            lambda: self.warp_symbols("eternal tilted", 0, 2),
            lambda: self.warp_symbols("blood tears", 0, 2),
            lambda: "hurt",
            lambda: "hopeless",
            lambda: f'{random.randint(8, 17)} y.o.',
            lambda: self.warp_symbols("sad", 0, 3),
            lambda: "sad",
            lambda: "1000-7",
            lambda: "чудище",
            lambda: "hate",
            lambda: "all mute",
            lambda: self.warp_symbols("hate", 0, 2),
            lambda: "666" * random.randint(1, 3),
            lambda: self.warp_symbols("bury me alive", 1, 3),
            lambda: '"i tired of this place"',
            lambda: self.warp_symbols("плевать на всех", 1, 3),
            lambda: self.warp_symbols("no brain", 0, 2),
            lambda: self.warp_symbols("feeling alive", 1, 3),
            lambda: "mode:",
            lambda: "mode:",
            lambda: "mode:",
            lambda: "pudge abuzer",
            lambda: "sf abuzer",
            lambda: "loser",
            lambda: "depressed",
            lambda: self.warp_symbols("white prince", 0, 3),
            lambda: self.warp_symbols("throw down your tears", 0, 2),
            lambda: "faceless",
            lambda: self.warp_symbols("emptiness", 0, 2),
            lambda: "hollow",
            lambda: "numbness",
            lambda: "suffered",
            lambda: "senseless",
            lambda: "abandoned",
            lambda: self.warp_symbols("everlasting hate", 0, 3),
            lambda: self.warp_symbols("let me die", 0, 3),
            lambda: "fearless",
            lambda: self.warp_symbols("blessed", 0, 2),
            lambda: "hopeless",
            lambda: self.warp_symbols("obsessed", 0, 2),
            lambda: "numb the pain",
            lambda: "tragic",
            lambda: self.warp_symbols("immortal", 0, 2),
            lambda: "weak",
            lambda: "rebellious",
            lambda: self.warp_symbols("cursed", 0, 2),
            lambda: self.warp_symbols("zxc god", 0, 3),
            lambda: self.warp_symbols("zxc king", 0, 3),
            lambda: self.warp_symbols("zxc demon", 0, 3),
            lambda: self.warp_symbols("zxc beast", 0, 3),
            lambda: "damaged",
            lambda: self.warp_symbols("dying as a lifestyle", 1, 3),
            lambda: self.warp_symbols("hate me as you do", 1, 2),
            lambda: self.warp_symbols("tilted", 0, 2),
            lambda: self.warp_symbols("ugly god", 0, 3),
            lambda: self.warp_symbols("ugly god", 0, 3),
            lambda: "дед инсайд если че",
            lambda: "broken",
            lambda: self.warp_symbols("kill me", 0, 3),
            lambda: "death",
            lambda: self.warp_symbols("death", 1, 3),
            lambda: "ghoul",
            lambda: self.warp_symbols("ghoul", 1, 3),
            lambda: self.warp_symbols("pain", 1, 3),
            lambda: self.warp_symbols("pain", 1, 3),
            lambda: random.choice(self.symbols),
            lambda: f"{random.randint(0, 9)}k pts",
            lambda: f'{random.choice(["SSS", "SS+", "SS", "S+", "S", "A", "B", "C"])} ранг',
            lambda: self.warp_symbols("drain", 0, 3),
            lambda: self.warp_symbols("schizophrenic", 0, 3),
            lambda: self.warp_symbols("emotionless", 0, 3),
            lambda: self.warp_symbols("chen abuzer", 0, 3),
            lambda: self.warp_symbols("amulet abuzer", 0, 3),
            lambda: self.warp_symbols("psiblades abuzer", 0, 3),
            lambda: "warden abuzer",
            lambda: "╰‿╯",
            lambda: "zitrax mode",
            lambda: self.warp_symbols("𝖌𝖍𝖔𝖚𝖑", 0, 3),
            lambda: self.warp_symbols("solo", 0, 3),
            lambda: "igrushka otchima",
            lambda: "watch me die",
            lambda: "nocturnal",
            lambda: self.warp_symbols("genius", 0, 3),
            lambda: self.warp_symbols("hatred", 0, 3),
            lambda: self.warp_symbols("doomed", 0, 3),
            lambda: self.warp_symbols("shining", 0, 3),
            lambda: self.warp_symbols("fearful", 0, 3),
            lambda: self.warp_symbols("bleeding", 0, 3),
            lambda: "demon",
            lambda: self.warp_symbols("leprotic", 0, 3),
            lambda: self.warp_symbols("savage", 0, 3),
            lambda: self.warp_symbols("epileptic", 0, 3),
            lambda: self.warp_symbols("drain", 0, 3),
            lambda: self.warp_symbols("crying", 0, 3),
            lambda: self.warp_symbols("anxiety", 0, 3),
            lambda: self.warp_symbols("toxic", 0, 3),
            lambda: self.warp_symbols("paranoid", 0, 3),
            lambda: self.warp_symbols("suicidal", 0, 3),
            lambda: self.warp_symbols("bipolar", 0, 3),
            lambda: "humiliated",
            lambda: self.warp_symbols("talentless", 0, 3),
        ]

    def warp_symbols(self, n, r, e):
        t = random.randint(r, e)
        o = ""
        for _ in range(t):
            o += random.choice(self.symbols)
        return f"{o}{n}{o[::-1]}"

    def generate(self):

        self.ghoul_count += 1

        if self.ghoul_count == self.ghoul_count_need:
            self.ghoul_count = 0
            self.ghoul_count_need = random.randint(3, 6)

        n = random.randint(2, 4)
        r = list(range(len(self.sfix)))
        e = ""
        for _ in range(n):
            index = random.choice(r)
            e += self.sfix[index]() + " "
            r.remove(index)

        return e


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # установка иконки
        image_path = os.path.join(os.path.dirname(__file__), "data", "icons", "icon1.ico")
        self.iconbitmap(image_path)

        # инициализация окна и названия
        self.geometry("800x600")
        self.title('Dota Fun')
        self.resizable(False, False)

        # объявление переменных
        self.self_select_hero_var = ctk.Variable(value=False)
        self.settings_visible = ctk.Variable(value=False)
        self.build_visible = ctk.Variable(value=True)
        self.nickname_visible = ctk.Variable(value=False)
        self.req_item_var = ctk.Variable()
        self.req_sapog_var = ctk.Variable()
        self.pizdec_var = ctk.Variable()
        self.nicky = None

        # создание шапки приложения
        self.top_frame = ctk.CTkFrame(master=self, fg_color='black', width=1000)
        self.top_frame.grid(row=0, column=0, padx=(1, 1), pady=(1, 0), sticky='nsew')

        # размещение логотипа
        image_path = os.path.join(os.path.dirname(__file__), "data", "icons", "000.png")
        self.logo = ctk.CTkImage(dark_image=Image.open(image_path), size=(148, 78))
        self.logo_label = ctk.CTkLabel(master=self.top_frame, text='', image=self.logo, fg_color='transparent')
        self.logo_label.grid(row=0, column=0, sticky='nw')

        # кнопка создания билда
        self.build_btn = ctk.CTkButton(master=self.top_frame, text='Build', width=100, command=self.show_build)
        self.build_btn.grid(row=0, column=1, padx=(150, 0), pady=25, sticky='nw')

        # кнопка создания ника
        self.nickname_btn = ctk.CTkButton(master=self.top_frame, text='Nickname', width=100, command=self.show_nickname)
        self.nickname_btn.grid(row=0, column=2, padx=(10, 400), pady=25, sticky='nw')

        # фрейм с никнеймами
        self.main_nickname_frame = ctk.CTkFrame(master=self, fg_color='transparent', width=800, height=600)

        # поле с ником
        self.textbox = ctk.CTkTextbox(master=self.main_nickname_frame, width=600, height=50, border_color='white',
                                      font=('Comic Sans MS', 16),
                                      corner_radius=20)
        self.textbox.grid(row=0, column=0, sticky="nsew", padx=100, pady=(100, 30))
        self.textbox.insert("0.0", 'Nickname')

        # кнопка генерации ника
        self.nickgenerate_btn = ctk.CTkButton(master=self.main_nickname_frame, width=100, text='Generate',
                                              command=self.set_name)
        self.nickgenerate_btn.grid(row=1, column=0, sticky='n')

        # кнопка копирования ника
        self.copy_btn = ctk.CTkButton(master=self.main_nickname_frame, width=100, text='Copy', command=self.copy_nick)
        self.copy_btn.grid(row=2, column=0, pady=(10, 300), sticky='n')

        # фрейм с билдом
        self.build_frame = ctk.CTkFrame(master=self, fg_color='transparent')
        self.build_frame.grid(row=1, column=0, sticky='nsew')

        # фрейм с настройками
        self.settings_frame = ctk.CTkFrame(master=self.build_frame, fg_color='transparent')
        self.settings_frame.grid(row=0, column=0, sticky='nw')

        # кнопка настройки генерации билда
        self.btn_settings = ctk.CTkButton(master=self.settings_frame, text='Settings', width=100,
                                          command=self.show_settings_frame)
        self.btn_settings.grid(row=0, column=0, padx=(30, 0), pady=(10, 0))

        # фрейм генерации
        self.generate_frame = ctk.CTkFrame(master=self.build_frame, fg_color='transparent')
        self.generate_frame.grid(row=1, column=0, padx=(100, 0), sticky='nsew')

        # кнопка генерации билда
        self.btn_generate = ctk.CTkButton(master=self.generate_frame, text='Generate', width=100,
                                          command=self.set_build)
        self.btn_generate.grid(row=0, column=0, padx=250, pady=(25, 25))

        # лейбл генерации героя
        self.hero_image_label = ctk.CTkLabel(master=self.generate_frame, text='')
        self.hero_image_label.grid(row=1, column=0, pady=10, sticky='n')

        # лейбл генерации таланта
        self.talent_image_label = ctk.CTkLabel(master=self.generate_frame, text='')
        self.talent_image_label.grid(row=1, column=0, padx=(200, 0), pady=10)

        # фрейм генерации предметов
        self.item_image_frame = ctk.CTkFrame(master=self.generate_frame, fg_color='transparent')
        self.item_image_frame.grid(row=2, column=0, pady=10, sticky='n')

        # фрейм настроек
        self.configure_frame = ctk.CTkFrame(master=self.settings_frame, fg_color='transparent')

        # комбобокс с героями
        self.combabox = ctk.CTkButton(master=self.configure_frame, text='Выбрать героя', width=250,
                                      fg_color='transparent', border_width=1)
        self.combabox.grid(row=2, column=1, padx=(0, 80), pady=10)
        CTkScrollableDropdown(self.combabox, values=[hero['name'] for hero in heroes], height=270, resize=False,
                              button_height=30, scrollbar=False, command=lambda e: self.combabox.configure(text=e))

        # лейбл "Выберите Героя"
        self.hero_selection_label = ctk.CTkLabel(master=self.configure_frame, text='Выберите героя')
        self.hero_selection_label.grid(row=2, column=0, padx=(0, 80), pady=10)

        # свитчер выбора своего героя
        self.self_select_hero_switch = ctk.CTkSwitch(master=self.configure_frame, text='Свой герой',
                                                     variable=self.self_select_hero_var)
        self.self_select_hero_switch.grid(row=3, column=0, columnspan=2, pady=10, padx=(0, 320))

        # свитчер обязательной кханды
        self.switch_req_item = ctk.CTkSwitch(master=self.configure_frame, text='Обязательная Khanda',
                                             variable=self.req_item_var)
        self.switch_req_item.grid(row=0, column=0)

        # свитчер обязательного сапога
        self.switch_sapog_item = ctk.CTkSwitch(master=self.configure_frame, text='Обязательный сапог',
                                               variable=self.req_sapog_var)
        self.switch_sapog_item.grid(row=1, column=0, pady=10)

        # свитчер фулл пиздец
        self.switch_pizdec = ctk.CTkSwitch(master=self.configure_frame, text='FullPizdec',
                                           variable=self.pizdec_var, border_color='red', text_color='red',
                                           progress_color='red')
        self.switch_pizdec.grid(row=0, column=1, pady=10, padx=50)

    def show_build(self):  # функция отображения билд-генерации
        if self.build_visible:
            pass
        else:
            self.build_frame.grid(row=1, column=0, sticky='nsew')
            self.settings_visible = True

    def show_nickname(self):  # функция отображения никнейм-генерации
        if not self.nickname_visible:
            pass
        else:
            self.build_visible = False
            self.build_frame.grid_forget()
            self.main_nickname_frame.grid(row=1, column=0, sticky='nsew')
            self.nickname_visible = True

    def show_settings_frame(self):  # функция отображения настроек
        if self.settings_visible:
            self.configure_frame.grid(row=1, column=1, padx=(30, 180), pady=(10, 10), sticky='nsew')
            self.settings_visible = False
        else:
            self.configure_frame.grid_forget()
            self.settings_visible = True

    def set_build(self):  # функция отображения героя и предметов
        global selected_hero
        global selected_items
        global selected_talant

        self.hero_image_label.configure(image=None)
        self.hero_image_label.image = None

        if self.self_select_hero_var.get():
            try:
                selected_hero_name = self.combabox.cget("text")
                selected_hero = [hero for hero in heroes if hero['name'] == selected_hero_name][0]
            except IndexError:
                selected_hero = random.choice(heroes)
        else:
            selected_hero = random.choice(heroes)

        hero_image_path = os.path.join(os.path.dirname(__file__), "data", "hero", selected_hero['image'])
        hero_image = ctk.CTkImage(dark_image=Image.open(hero_image_path), size=(128, 72))
        self.hero_image_label.configure(image=hero_image)
        self.hero_image_label.image = hero_image

        selected_talant = random.choice(talants)
        talant_image_path = os.path.join(os.path.dirname(__file__), "data", "talants", selected_talant['image'])
        talant_image = ctk.CTkImage(dark_image=Image.open(talant_image_path), size=(80, 80))
        self.talent_image_label.configure(image=talant_image)
        self.talent_image_label.image = talant_image

        item_limit = 6
        selected_items = []
        if not self.pizdec_var.get():
            if self.req_item_var.get() and self.req_sapog_var.get():
                required_item = items[45]
                sapog = random.choice([item for item in sapogi if item['name'] not in selected_items])
                selected_items.append(sapog)
                selected_items.append(required_item)
            elif self.req_item_var.get():
                required_item = items[45]
                selected_items.append(required_item)
            elif self.req_sapog_var.get():
                sapog = random.choice(sapogi)
                selected_items.append(sapog)
            while len(selected_items) < item_limit:
                random_item = random.choice(items)
                if random_item not in selected_items and random_item not in sapogi:
                    selected_items.append(random_item)
        else:
            while len(selected_items) < item_limit:
                random_item = random.choice(items)
                selected_items.append(random_item)

        self.display_items(selected_items)

    def display_items(self, selected_itemss):  # функция отображения предметов
        self.item_image_frame.destroy()
        self.item_image_frame = ctk.CTkFrame(master=self.generate_frame, fg_color='transparent')
        self.item_image_frame.grid(row=2, column=0, pady=10, sticky='n')

        for i, item in enumerate(selected_itemss):
            item_image_path = os.path.join(os.path.dirname(__file__), "data", "items", item['image'])
            item_image = ctk.CTkImage(dark_image=Image.open(item_image_path), size=(88, 64))

            item_image_label = ctk.CTkLabel(master=self.item_image_frame, text='')
            item_image_label.grid(row=0, column=i, padx=5)
            item_image_label.configure(image=item_image)
            item_image_label.image = item_image

    def set_name(self):
        a = GenerateNick()
        self.nicky = a.generate()
        self.textbox.delete("0.0", 'end')
        self.textbox.insert("0.0", self.nicky)

    def copy_nick(self):
        pyperclip.copy(self.nicky)


if __name__ == '__main__':
    app = App()
    app.mainloop()
