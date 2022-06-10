using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003639: Greg
/// </summary>
public class _11003639 : NpcScript {
    internal _11003639(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009103$ 
                // - Retiring here is the best choice I ever made! 
                return true;
            case 10:
                // $script:1109121007009104$ 
                // - You here to see the fight? I never miss a match. I even brought my own binoculars so I can see every drop of sweat and every knocked-out tooth! 
                switch (selection) {
                    // $script:1109121007009105$
                    // - Nah, I'm not into blood sports.
                    case 0:
                        Id = 11;
                        return false;
                    // $script:1109121007009106$
                    // - Sure am! I'm a huge fan.
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009107$ 
                // - Really? Huh. Never thought $npcName:11003535[gender:1]$ would recruit an agent with such a weak stomach. 
                switch (selection) {
                    // $script:1109121007009108$
                    // - Ah, so you're with Dark Wind.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009109$ 
                // - I knew I liked you the moment I saw you! $npcName:11003535[gender:1]$'s got great taste in agents. 
                switch (selection) {
                    // $script:1109121007009110$
                    // - Ah, so you're with Dark Wind.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009111$ 
                // - Anyway, you're here for my special message, right? "Mask. Duck butt. Beast." 
                switch (selection) {
                    // $script:1109121007009112$
                    // - I'll pass that along.
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:1109121007009113$ 
                // - Shush! The fight's about to start! 
                return true;
            default:
                return true;
        }
    }
}
