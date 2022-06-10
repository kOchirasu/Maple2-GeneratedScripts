using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003257: Cheshire Carmen Bella Jr. II
/// </summary>
public class _11003257 : NpcScript {
    internal _11003257(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008184$ 
                // - Meow! 
                return true;
            case 30:
                // $script:0403155707008185$ 
                // - What're you staring at? Never see a talking cat before? 
                switch (selection) {
                    // $script:0403155707008186$
                    // - Guh...
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0403155707008187$
                    // - Are you a magic kitty?
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0403155707008188$ 
                // - Meheh! You're an old-fashioned one, talking animals are all the rage these days! I forgive your ignorance, though... so long as you bring me snacks next time. 
                return true;
            case 32:
                // $script:0403155707008189$ 
                // - Yep! A magical kitty for a magical place. This is $map:02000023$ after all, land of wonder and imagination. Welcome! 
                return true;
            case 40:
                // $script:0403155707008190$ 
                // - What's with the sour face? 
                switch (selection) {
                    // $script:0530154407008542$
                    // - Send me to $npcName:11003254[gender:1]$.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0530154407008543$ 
                // - Has my magic failed? Impossible! 
                switch (selection) {
                    // $script:0530154407008544$
                    // - Hurry it up!
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0530154407008545$ functionID=1 
                // - I'm trying! Close your eyes. It'll work for sure this time! 
                return true;
            case 50:
                // $script:0530154407008546$ 
                // - There's something... dark blocking my magic. There's no way to get to Ellinel right now.  
                return true;
            case 60:
                // $script:0530154407008547$ 
                // - What's with the sour face? 
                switch (selection) {
                    // $script:0808093807008794$
                    // - I'm lost.
                    case 0:
                        Id = 61;
                        return false;
                    // $script:0808122107008796$
                    // - I'm not depressed.
                    case 1:
                        Id = 62;
                        return false;
                }
                return true;
            case 61:
                // $script:0808122107008797$ 
                // - On to the next portal! Since you've passed through the gate to $map:02000023$, the portal there will open new paths to you. But if there's nowhere to go, the portal won't work. 
                return true;
            case 62:
                // $script:0808122107008798$ 
                // - You look worried. Go ahead, put your feet up and tell me your troubles. 
                return true;
            default:
                return true;
        }
    }
}
