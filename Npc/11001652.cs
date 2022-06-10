using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001652: Suspicious Man
/// </summary>
public class _11001652 : NpcScript {
    internal _11001652(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0519143707006208$ 
                // - ... 
                return true;
            case 30:
                // $script:0630142807006512$ 
                // - What's taking him so long...? Huh? What do you want?!
                switch (selection) {
                    // $script:0630142807006513$
                    // - What are you up to?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0630142807006514$ 
                // - Wh-what do you think? I'm sorting junk, that's what!
                switch (selection) {
                    // $script:0630142807006515$
                    // - (Stare at him.)
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0630142807006516$ 
                // - I-I'm not up to anything bad. Really. I'm just...
                // $script:0630142807006517$ 
                // - Wait. You're...
                switch (selection) {
                    // $script:0630142807006518$
                    // - You know me?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0630142807006519$ 
                // - You're the Gray Wolf! I was there when you took down those Blackstar goons in $map:02000138$.
                switch (selection) {
                    // $script:0630142807006520$
                    // - You're thinking of someone else.
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:0630142807006521$ 
                // - No, I'm not. You trying to stay off the radar? I would, too, if I had as many enemies as you. But your face has been burned into my brain ever since that day.
                switch (selection) {
                    // $script:0630142807006522$
                    // - ...
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:0630142807006523$ 
                // - Anyway, what are you doing here?
                switch (selection) {
                    // $script:0630142807006524$
                    // - I have business here.
                    case 0:
                        Id = 36;
                        return false;
                }
                return true;
            case 36:
                // $script:0630142807006525$ 
                // - Here? You and the Blackstars are mortal enemies now, right? Wait... you didn't come here to take them on at their headquarters, did you?
                switch (selection) {
                    // $script:0630142807006526$
                    // - Things... got a little out of control.
                    case 0:
                        Id = 37;
                        return false;
                }
                return true;
            case 37:
                // $script:0630142807006527$ 
                // - Y-you really are the terror of $map:02000138$! The equal of a hundred warriors! Y'know, I used to think you were just another thug... Since you're here, maybe there's a question you can answer for me. 
                // $script:0630142807006528$ 
                // - I have a, uh, "friend" who went inside their headquarters. He should have been able to sneak out while you kept the gangsters busy, but he's still missing. You didn't see anyone... suspicious when you were there, did you?
                switch (selection) {
                    // $script:0630142807006529$
                    // - Everyone in there looked suspicious.
                    case 0:
                        Id = 38;
                        return false;
                }
                return true;
            case 38:
                // $script:0630142807006530$ 
                // - Yeah, yeah, good point. Ha, I almost feel sorry for the Blackstars, having an enemy like you. Hahaha!
                switch (selection) {
                    // $script:0630142807006531$
                    // - (Say nothing.)
                    case 0:
                        Id = 39;
                        return false;
                }
                return true;
            case 39:
                // $script:0630142807006532$ 
                // - Ha... Ha ha... Ahem. You're a pretty intense $male:guy,female:gal$, you know that? I hope we meet again.
                return true;
            default:
                return true;
        }
    }
}
