using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000527: Hermit
/// </summary>
public class _11000527 : NpcScript {
    internal _11000527(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002251$ 
                // - Welcome. It's nice to meet you. 
                return true;
            case 30:
                // $script:0831180407002254$ 
                // - $MyPCName$, I can't believe we're meeting again like this. I can see in your eyes how much you've grown since last we met. Do you remember what I told you then? That the world would need a hero?  
                // $script:0831180407002255$ 
                // - Looking at you now, I believe that you're the one. 
                return true;
            case 40:
                // $script:0831180407002256$ 
                // - Ha ha ha, you look like you have many questions for me. What do you want to know? 
                switch (selection) {
                    // $script:0831180407002257$
                    // - How did you end up on Victoria Island?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0831180407002258$
                    // - Why did you save $npcName:11000064[gender:0]$?
                    case 1:
                        Id = 43;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002259$ 
                // - This $map:02000051$ is where I was born and raised. The last time I left, I swore I'd never return... I thought that was best for everyone here.  
                // $script:0831180407002260$ 
                // - But something happened, and it made me wonder if I made the right decision. I came back to finish what I couldn't finish then. 
                switch (selection) {
                    // $script:0831180407002261$
                    // - What is it?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0831180407002262$ 
                // - That's... I'll tell you when I'm ready. 
                return true;
            case 43:
                // $script:0831180407002263$ 
                // - I couldn't ignore the wish of a dying man. Even if he was a prisoner...  
                // $script:0831180407002264$ 
                // - And when he awoke after his brush with death, I could see in his eyes that he was innocent. I didn't ask any questions, but I knew I had to help him. 
                // $script:0831180407002265$ 
                // - Stay true to yourself, and you can overcome anything. No matter how difficult it is, you can do it. 
                return true;
            case 50:
                // $script:0809153207007164$ 
                // - Every age needs a hero. 
                return true;
            default:
                return true;
        }
    }
}
