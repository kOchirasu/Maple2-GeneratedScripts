using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000757: 
/// </summary>
public class _11000757 : NpcScript {
    internal _11000757(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180306000296$ 
                // - $npc:11000735[gender:1]$ is the best, but...  
                return true;
            case 30:
                // $script:0831180306000299$ 
                // - They're so loud. Why do they think $npcName:11000406[gender:0]$ is handsome anyway? If they saw $npcName:11000735[gender:1]$, they'd never look at $npcName:11000406[gender:0]$ the same way again.   
                // $script:0831180306000300$ 
                // - $MyPCName$, have you met $npc:11000735[gender:1]$? 
                switch (selection) {
                    // $script:0831180306000301$
                    // - I know all about $npcName:11000735[gender:1]$.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180306000302$
                    // - Who's $npcName:11000735[gender:1]$?
                    case 1:
                        Id = 32;
                        return false;
                    // $script:0831180306000303$
                    // - $npcName:11000406[gender:0]$'s the best!
                    case 2:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180306000304$ 
                // - You mean you really have seen $npcName:11000735[gender:1]$? I saw her once.  
                // $script:0831180306000305$ 
                // - It was only for a moment, but it was like seeing a brilliant shooting star shining against the darkness of the sky. In that moment, $npcName:11000735[gender:1]$'s wondrous image became imprinted in my mind as if it were a photograph, and I was never the same again. 
                // $script:0831180306000306$ 
                // - Since then, it's been my dearest wish to see $npcName:11000735[gender:1]$ again. I've reminisced with others about her and painted dozens of pictures of her based on that single, beautiful memory. 
                // $script:0831180306000307$ 
                // - In these paintings, I strive to encapsulate even a small part of $npcName:11000735[gender:1]$'s celestial charm. The reflection of her soul is like an ever-changing sky, bright as a summer's day or stormy as the darkest winter's night... 
                return true;
            case 32:
                // $script:0831180306000308$ 
                // - I may have only seen her once, but I know the wonder of her soul. She appears as swiftly as the wind and disappears just as soon. Fleeting as my time with her has been, I know she's the woman of my dreams! 
                // $script:0831180306000309$ 
                // - Until the day I can profess my true love for her brilliant soul, I shall paint and expound upon her many wonders to those who would share my appreciation. 
                return true;
            case 33:
                // $script:0831180306000310$ 
                // - You're just like the squealing girls over there. You'll change your mind if you see $npcName:11000735[gender:1]$ even once.  
                return true;
            default:
                return true;
        }
    }
}
