using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000757: 
/// </summary>
public class _11000757 : NpcScript {
    protected override void FirstScript() {
        (Id, Button) = (30, NpcTalkButton.Next);
    }

    protected override (int, NpcTalkButton) Next(int selection) {
        switch (Id) {
            case 0:
                // $script:0831180306000296$ 
                // - $npc:11000735[gender:1]$ is the best, but... 
                return default;
            case 30:
                switch (Index++) {
                    case 0:
                        // $script:0831180306000299$ 
                        // - They're so loud. Why do they think $npcName:11000406[gender:0]$ is handsome anyway? If they saw $npcName:11000735[gender:1]$, they'd never look at $npcName:11000406[gender:0]$ the same way again.  
                        return (30, NpcTalkButton.SelectableDistractor);
                    case 1:
                        // $script:0831180306000300$ 
                        // - $MyPCName$, have you met $npc:11000735[gender:1]$?
                        switch (selection) {
                            // $script:0831180306000301$
                            // - I know all about $npcName:11000735[gender:1]$.
                            case 0:
                                return (31, NpcTalkButton.Next);
                            // $script:0831180306000302$
                            // - Who's $npcName:11000735[gender:1]$?
                            case 1:
                                return (32, NpcTalkButton.Next);
                            // $script:0831180306000303$
                            // - $npcName:11000406[gender:0]$'s the best!
                            case 2:
                                return (33, NpcTalkButton.Close);
                        }
                        return default;
                }
                break;
            case 31:
                switch (Index++) {
                    case 0:
                        // $script:0831180306000304$ 
                        // - You mean you really have seen $npcName:11000735[gender:1]$? I saw her once. 
                        return (31, NpcTalkButton.Next);
                    case 1:
                        // $script:0831180306000305$ 
                        // - It was only for a moment, but it was like seeing a brilliant shooting star shining against the darkness of the sky. In that moment, $npcName:11000735[gender:1]$'s wondrous image became imprinted in my mind as if it were a photograph, and I was never the same again.
                        return (31, NpcTalkButton.Next);
                    case 2:
                        // $script:0831180306000306$ 
                        // - Since then, it's been my dearest wish to see $npcName:11000735[gender:1]$ again. I've reminisced with others about her and painted dozens of pictures of her based on that single, beautiful memory.
                        return (31, NpcTalkButton.Close);
                    case 3:
                        // $script:0831180306000307$ 
                        // - In these paintings, I strive to encapsulate even a small part of $npcName:11000735[gender:1]$'s celestial charm. The reflection of her soul is like an ever-changing sky, bright as a summer's day or stormy as the darkest winter's night...
                        return default;
                }
                break;
            case 32:
                switch (Index++) {
                    case 0:
                        // $script:0831180306000308$ 
                        // - I may have only seen her once, but I know the wonder of her soul. She appears as swiftly as the wind and disappears just as soon. Fleeting as my time with her has been, I know she's the woman of my dreams!
                        return (32, NpcTalkButton.Close);
                    case 1:
                        // $script:0831180306000309$ 
                        // - Until the day I can profess my true love for her brilliant soul, I shall paint and expound upon her many wonders to those who would share my appreciation.
                        return default;
                }
                break;
            case 33:
                // $script:0831180306000310$ 
                // - You're just like the squealing girls over there. You'll change your mind if you see $npcName:11000735[gender:1]$ even once. 
                return default;
        }
        
        return default;
    }
}
