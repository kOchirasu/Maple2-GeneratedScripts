using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000510: Peachy
/// </summary>
public class _11000510 : NpcScript {
    internal _11000510(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123232210001189$ 
                // - I better take a break from the forge and do some finishing. Did you see my jig or wire brush around?
                return true;
            case 10:
                // $script:1123232210001193$ 
                // - Just a quick rap on the anvil to break off the fire scale, and this sword is done... Oh, hello. Have you come to enchant your gear?
                switch (selection) {
                    // $script:1123232210001194$
                    // - Can you enchant my items?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0323154410001466$
                    // - How about we change some bonus attributes?
                    case 1:
                        Id = 30;
                        return false;
                    // $script:0323154410001467$
                    // - Tell me about your work.
                    case 2:
                        Id = 29;
                        return false;
                }
                return true;
            case 29:
                // $script:1123232210001196$ 
                // - Hehe. I'm a blacksmith.
                // $script:1123232210001197$ 
                // - I love the work that I do. There's nothing more satisfying than using my wrench to tinker with gear or banging metal into shape in front of a hot forge.
                // $script:1123232210001198$ 
                // - If you need to strengthen your equipment, come to me! You'll have to gather the materials: $itemPlural:40100001$, $itemPlural:40100023$, and $itemPlural:40100024$.
                // $script:1123232210001199$ 
                // - You can get $itemPlural:40100023$ by dismantling level 20 or higher gear. Just use the Dismantle button in your inventory window. As for $itemPlural:40100024$, they'll only come from dismantling gear that's epic or better.
                // $script:1123232210001200$ 
                // - People also compete for $itemPlural:40100023$ at the Maple Arena, if that's something you're interested in.
                // $script:1123232210001201$ 
                // - I used to enchant low level gear for people, but we all soon realized it's just not worth it. So now, I only enchant items marked as "Can be Enchanted."
                // $script:0323154410001468$ 
                // - Oh! One more thing! I'm sure you know that some high-grade gear grant random special abilities. If you're interested in modifying those abilities, I can help!
                // $script:0323154410001469$ 
                // - This is a brand new service blacksmiths can provide, thanks to a breakthrough at the $map:02000270$ research center. Hehe. They've refined meteoric ores into $itemPlural:40100026$ that can change the chemical properties in gear!
                // $script:0323154410001470$ 
                // - Of course, bonus attributes are hard to rely on since the results are so random. And in addition to $itemPlural:40100026$, you'll also need $itemPlural:40100001$, $itemPlural:40100002$, $itemPlural:40100003$, or $itemPlural:40100021$, depending on the work being done.
                return true;
            case 30:
                // $script:0323154410001471$ functionID=1 
                // - Oh! Of course! Just pick an item for me to work on. Remember, I only handle epic and legendary armor and accessories level 50 and above.
                return true;
            case 31:
                // $script:1123232210001202$ functionID=1 
                // - Oh! Sure thing! Select an item for me to enchant. It's got to have the "Can be Enchanted" mark on it, you hear?
                return true;
            case 999:
                // $script:1123232210001278$ 
                // - I'm so sorry! I'm swamped! Never been so busy in my life. I'm working on a special order, you see.
                switch (selection) {
                    // $script:1123232210001279$
                    // - Can you enchant my items?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:1123232210001280$
                    // - What do you do?
                    case 1:
                        Id = 39;
                        return false;
                }
                return true;
            case 39:
                // $script:1123232210001281$ 
                // - Hehe. I'm a blacksmith.
                // $script:1123232210001282$ 
                // - I love the work that I do. There's nothing more satisfying than using my wrench to tinker with gear or banging metal into shape in front of a hot forge.
                // $script:1123232210001283$ 
                // - If you need to strengthen your equipment, come to me! You'll have to gather the materials: $itemPlural:40100001$, $itemPlural:40100023$, and $itemPlural:40100024$.
                // $script:1123232210001284$ 
                // - You can get $itemPlural:40100023$ by dismantling level 20 or higher gear. Just use the Dismantle button in your inventory window. As for $itemPlural:40100024$, they'll only come from dismantling gear that's epic or better.
                // $script:1123232210001285$ 
                // - People also compete for $itemPlural:40100023$ at the Maple Arena, if that's something you're interested in.
                // $script:1123232210001286$ 
                // - Some customers desire for me to enchant low level gear, but it's simply not worth the time. I only enchant items marked as "Can be Enchanted."
                return true;
            case 41:
                // $script:1123232210001287$ 
                // - I'd love to help you, but for now I have to focus on this special order I've got. I'll take especially good care of you if you come back later, I promise.
                return true;
            default:
                return true;
        }
    }
}
