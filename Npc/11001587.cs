using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001587: Ishura
/// </summary>
public class _11001587 : NpcScript {
    internal _11001587(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006075$ 
                // - Ah, $MyPCName$! 
                return true;
            case 10:
                // $script:0515180307006123$ 
                // - There must be something about the power $npcName:11001231[gender:0]$  seeks in our ancestors' records. 
                switch (selection) {
                    // $script:0515180307006124$
                    // - Why are you so sure?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0515180307006125$ 
                // - I encountered Holstatt in the Land of Darkness once. He said that Arazaad had kept a secret from us. That the real legacy of our ancestors was elsewhere.  
                // $script:0515180307006126$ 
                // - I don't know if he was lying or not. But if he wasn't, then the old records, which only Arazaad could read, must hold clue about the secret. Something to point us towards this so-called legacy.  
                return true;
            case 20:
                // $script:0517210007006136$ 
                // - Why are you staring at me? 
                switch (selection) {
                    // $script:0517210007006137$
                    // - I just wanted to see you.
                    case 0:
                        Id = 21;
                        return false;
                    // $script:0517210007006138$
                    // - I missed you so much!
                    case 1:
                        Id = 22;
                        return false;
                    // $script:0517210007006139$
                    // - Play with me.
                    case 2:
                        Id = 23;
                        return false;
                    // $script:0517210007006140$
                    // - There's something I need to tell you.
                    case 3:
                        Id = 24;
                        return false;
                }
                return true;
            case 21:
                // $script:0517210007006141$ 
                // - Ha... Weirdo...  
                return true;
            case 22:
                // $script:0517210007006142$ 
                // - Y-you did? So did I. Ahem. 
                return true;
            case 23:
                // $script:0517210007006143$ 
                // - Now is <i>not</i> the time for such things! 
                return true;
            case 24:
                // $script:0517210007006144$ 
                // - I'm a little busy right now. 
                return true;
            case 30:
                // $script:0524142307006216$ 
                // - There must be something about the power $npcName:11001231[gender:0]$ seeks in our ancestors' records. 
                switch (selection) {
                    // $script:0524142307006217$
                    // - Why are you so sure?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0524142307006218$ 
                // - I encountered Holstatt in the Land of Darkness once. He said that Arazaad had kept a secret from us. That the real legacy of our ancestors was elsewhere.  
                return true;
            case 32:
                // $script:0524142307006219$ 
                // - I don't know if he was lying or not. But if he wasn't, then the old records, which only Arazaad could read, must hold some clue about the secret. Something to point us towards this so-called legacy.  
                return true;
            default:
                return true;
        }
    }
}
