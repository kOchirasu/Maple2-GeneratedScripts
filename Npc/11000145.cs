using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000145: Andy
/// </summary>
public class _11000145 : NpcScript {
    internal _11000145(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000611$ 
                // - What brings you here? 
                return true;
            case 20:
                // $script:0831180407000613$ 
                // - Ugh... I feel dizzy...  
                switch (selection) {
                    // $script:0831180407000614$
                    // - Who are you?
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407000615$ 
                // - Name's $npcName:11000145[gender:0]$. You? 
                switch (selection) {
                    // $script:0831180407000616$
                    // - I'm $MyPCName$.
                    case 0:
                        Id = 22;
                        return false;
                }
                return true;
            case 22:
                // $script:0831180407000617$ 
                // - $MyPCName$? That sounds familiar... Was that when I lost my pocket watch? 
                switch (selection) {
                    // $script:0831180407000618$
                    // - Do you know me?
                    case 0:
                        Id = 23;
                        return false;
                }
                return true;
            case 23:
                // $script:0831180407000619$ 
                // - Oh, no. Your name just sounds familiar to me. I've been to so many places that sometimes I get names mixed up. Being here in the past is really...  
                // $script:0831180407000620$ 
                // - Ahh, never mind. I'm talking nonsense now. Sigh... If you'll excuse me, I have things to do...  
                return true;
            case 30:
                // $script:0831180407000621$ 
                // - I'm sorry, but there's nothing more I can tell you about $npcName:22000322[gender:0]$ or the strange man wearing a $item:11300119$. Or, wait, have you asked yet? 
                return true;
            default:
                return true;
        }
    }
}
