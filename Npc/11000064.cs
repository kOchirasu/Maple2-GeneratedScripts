using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000064: Lennon
/// </summary>
public class _11000064 : NpcScript {
    internal _11000064(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000315$ 
                // - It's good to see you.
                return true;
            case 30:
                // $script:0831180407000318$ 
                // -  I couldn't have returned to my old life if it weren't for the people who believed in me. 
                // $script:0831180407000319$ 
                // -  $MyPCName$, you've helped me so much. Thank you.
                return true;
            case 40:
                // $script:0831180407000320$ 
                // - When I was a fugitive, you gave me a run for my money a few times.
                switch (selection) {
                    // $script:0831180407000321$
                    // - Really? That's not how I remember it.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407000322$ 
                // - You have no idea. There were a few times that you were only a few feet away from me. If you'd looked around the wrong corner...
                // $script:0831180407000323$ 
                // - Luckily, in the end, you decided to trust $npcName:11000529[gender:0]$ instead of $npcName:11000044[gender:0]$. If you'd gone the other way, who knows how things would have turned out?
                switch (selection) {
                    // $script:0831180407000324$
                    // - You were doing pretty well on your own.
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0831180407000325$ 
                // - Maybe it looked like that from the outside, but I was backed into a corner. Bella forced my hand at Katramus. Without you and Blackeye, I'd probably be dead now.
                // $script:0831180407000326$ 
                // - In those early days, I didn't think much of you. But no matter how many false leads I planted, you were always back on my tail within a matter of hours.
                // $script:0831180407000327$ 
                // - I was sure you'd give up after our fight in that abandoned townhouse. But you kept on growing stronger after that. If I had to fight you now...
                // $script:0831180407000328$ 
                // - Let's just say that I'm glad we're on the same side.
                return true;
            case 50:
                // $script:0831180407000329$ 
                // - We used to be best friends, Katvan, Eve, and I. We got into all kinds of mischief when we were kids...
                // $script:0831180407000330$ 
                // - But that just makes me hate him more. We had bonds that were thicker than blood, and he betrayed us. For what? A fancy title and a little bit of power?
                // $script:0831180407000331$ 
                // - Eve thinks that he might come around again. But I know better. I know Katvan's true colors.
                switch (selection) {
                    // $script:0831180407000332$
                    // - Surely there's more to the story.
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407000333$ 
                // - Of course there's more to the story. There's the part that's still coming up. The part where I put Katvan in the ground once and for all.
                // $script:0831180407000334$ 
                // - He killed my mentor–Eve's father! There's nothing left to talk about.
                // $script:0831180407000335$ 
                // - He had me on the ropes before, but things are different now. And I know I can count on you to help me take him out.
                return true;
            default:
                return true;
        }
    }
}
