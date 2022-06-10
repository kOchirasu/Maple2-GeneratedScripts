using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000289: Screaming Fist
/// </summary>
public class _11000289 : NpcScript {
    internal _11000289(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001130$ 
                // - What is it? 
                return true;
            case 50:
                // $script:0831180407001133$ 
                // - Hey, hey! I'm in the middle of practice. Get out of the way! 
                switch (selection) {
                    // $script:0831180407001134$
                    // - What are you doing?
                    case 0:
                        Id = 51;
                        return false;
                    // $script:0831180407001135$
                    // - Sell me on this $map:2000217$ business.
                    case 1:
                        Id = 52;
                        return false;
                    // $script:0831180407001136$
                    // - How can I join the Maple Arena?
                    case 2:
                        Id = 53;
                        return false;
                    // $script:0831180407001137$
                    // - How can I crush my opponents?
                    case 3:
                        Id = 54;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407001138$ 
                // - Do you not see? I'm practicing my art. I cannot lose to $npcName:11000018[gender:0]$ again... He beat me once in the $map:65000001$ and he never shuts up about it! 
                // $script:0831180407001139$ 
                // - I'm never going to lose again! I'll show him what a mighty Murpagoth can do, and earn the praise of the Great Chief! 
                // $script:0831180407001140$ 
                // - Are you interested in competing against others? Er, that means you're a competitor! I have to practice. Please don't interrupt! 
                return true;
            case 52:
                // $script:0831180407001141$ 
                // - Hah! Toh! Huh? You look lost. This is an old arena that has existed for generations. 
                // $script:0831180407001142$ 
                // - Since ancient times, this $map:2000051$ has been home to us Murpagoths and the other tribes... Pigming, Kaka, Kolopupu, and T'oomba. The tribes were always at odds over their different beliefs and habits. 
                // $script:0831180407001143$ 
                // - Every time a conflict arose, the tribes would settle it at $map:2000217$. Fight it out fair and square, that was the rule of the day. But as time passed, a lot of things happened, and... Anyway, now the arena is open to all who wish to test their might.
 
                // $script:0831180407001144$ 
                // - There are two types of arenas: Maple Arena and Event PvP. To access the Maple Arena, open the Arena menu and register. Event PvP is accessed through the Event Notifications menu when it's available. 
                return true;
            case 53:
                // $script:0831180407001145$ 
                // - You want to join the Maple Arena? No problem. See the Arena menu at the bottom right side of the screen? Open the menu and select Register. The arena managers will let you know when they find an opponent for you, and they search every 5 minutes. 
                // $script:0831180407001146$ 
                // - When you select an opponent, you will get a notification asking if you're ready to enter the Arena. Press Enter Now to move instantly to the Arena. Easy, isn't it? 
                // $script:0831180407001147$ 
                // - Keep this in mind, though... If you get matched up but refuse to enter, you'll get a loss and be locked out of the arena for a short time. 
                // $script:0831180407001148$ 
                // - That means that if you register for the arena, you must enter it when you find an opponent. Cowards are not welcome in the arena! 
                // $script:0915102707003926$ 
                // - To ensure everyone's safety $npc:11000134[gender:0]$ has decreed that only those <font color="#ffd200">Level 50 or above</font> be allowed to enter the Arena. The Chief's word is law. 
                return true;
            case 54:
                // $script:0831180407001150$ 
                // - Looking to make a name for yourself in the arena? Hmmm... I had a feeling about you. If you can score some victories, perhaps you'll get the attention of $npcName:11000134[gender:0]$. It's the greatest honor the warriors of my tribe can strive for. 
                // $script:0831180407001151$ 
                // - That's not all, either. $npcName:11000134[gender:0]$ has ordered that warriors who prove their skill and valor be rewarded with $itemPlural:90000006$. With $itemPlural:90000006$, you can buy a variety of items at the Arena Shop. 
                // $script:0831180407001152$ 
                // - The Arena Shop sells equipment that will make you more powerful in the arena. If you're trying the arena for the first time, then the arena equipment sold for mesos is pretty useful, too. If you want the good stuff, though, you'll need $itemPlural:90000006$. 
                return true;
            default:
                return true;
        }
    }
}
