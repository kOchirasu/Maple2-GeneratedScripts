using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001630: Vasara Chen
/// </summary>
public class _11001630 : NpcScript {
    internal _11001630(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516130207006132$ 
                // - What brings you here?
                return true;
            case 20:
                // $script:0531170907006286$ 
                // - What is it now?
                switch (selection) {
                    // $script:0531170907006287$
                    // - Did you know about $npcName:11001629[gender:0]$'s plan?
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0531170907006288$ 
                // - Not that I think you'll believe me, but no, I didn't. Even if I did know, so what? It's not my job to stop him.
                switch (selection) {
                    // $script:0531170907006289$
                    // - Then you're no better than $npcName:11001629[gender:0]$.
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0531170907006290$ 
                // - Listen. My old man and I don't always see eye to eye, but he built Blackstar from the ground up. You gotta be ruthless to succeed in this town, and he's earned my respect.
                switch (selection) {
                    // $script:0531170907006291$
                    // - Old man... You're $npcName:11001629[gender:0]$'s son?!
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:0531170907006292$ 
                // - I didn't tell you? Must've slipped my mind. $npcName:11001630[gender:0]$, son of $npcName:11001629[gender:0]$, at your service.
                switch (selection) {
                    // $script:0531170907006293$
                    // - Slipped your mind. Sure.
                    case 0:
                        Id = 60;
                        return false;
                }
                return true;
            case 60:
                // $script:0531170907006294$ 
                // - Hey, where's it written that I have to tell every idiot who stumbles in here who my dad is? Now, get out of my face before I get mad.
                switch (selection) {
                    // $script:0531170907006295$
                    // - I'm not done with you.
                    case 0:
                        Id = 70;
                        return false;
                }
                return true;
            case 70:
                // $script:0531170907006296$ 
                // - Me neither. I got a feeling we'll be fighting again real soon. And next time, I'll beat you fair and square. No tricks.
                switch (selection) {
                    // $script:0531170907006297$
                    // - I'll see you in the ring.
                    case 0:
                        Id = 80;
                        return false;
                }
                return true;
            case 80:
                // $script:0531170907006298$ 
                // - Count on it.
                return true;
            default:
                return true;
        }
    }
}
