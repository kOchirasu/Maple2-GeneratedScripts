using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004336: Aisha
/// </summary>
public class _11004336 : NpcScript {
    internal _11004336(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010140307011595$ 
                // - These readings are off the chart!
                return true;
            case 10:
                // $script:1010140307011596$ 
                // - Is this for real?!
                switch (selection) {
                    // $script:1010153807011618$
                    // - Huh? What happened?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1010140307011597$ 
                // - Nothing <i>happened.</i> It's just... this place! I've never seen magic and science mashed together like this!
                // $script:1010140307011598$ 
                // - I need to get my hands on some of this aetherine stuff. If my calculations are right, the energy content of each of these little stones is... Well, it's explosive!
                // $script:1010140307011599$ 
                // - This could totally change how we think about energy!
                switch (selection) {
                    // $script:1010140307011600$
                    // - A bit of an energy nut, aren't you?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1010140307011601$ 
                // - Why wouldn't I be? This gives me an idea for a new reactor design...
                return true;
            case 40:
                // $script:1010151207011604$ 
                // - You—?!
                switch (selection) {
                    // $script:1010151207011605$
                    // - $npcName:11004336[gender:1]$?!
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1010153807011619$ 
                // - Boss! I was starting to think you didn't see me. Heh!
                // $script:1010151207011606$ 
                // - Keep your voice down, Boss! $npcName:11004334[gender:1]$ is right around the corner.
                switch (selection) {
                    // $script:1010151207011607$
                    // - Is that why you're here? To spy on the Resistance?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1010151207011608$ 
                // - No way! I'm here for critical research. At least, that's what I told $npcName:11000264[gender:0]$...
                // $script:1010151207011609$ 
                // - Boss, there's something you need to know. I've spotted the Resistance going in and out of $npcName:11000264[gender:0]$'s office.
                // $script:1010151207011610$ 
                // - They're up to something. Since I didn't know when you'd come visit me again, I decided I'd check it out for myself!
                switch (selection) {
                    // $script:1010151207011611$
                    // - This place is way too dangerous for you. Let's get you ba—
                    case 0:
                        Id = 43;
                        return false;
                }
                return true;
            case 43:
                // $script:1010151207011612$ 
                // - Uh, heck no! Even if I lied to my fake boss, there really <i>is</i> a ton of stuff for me to research here.
                // $script:1010151207011613$ 
                // - Anyway, you're too busy to save the world <i>and</i> spy on the Resistance. You need my help!
                switch (selection) {
                    // $script:1010151207011614$
                    // - $npcName:11004336[gender:1]$... By any chance, do you... have a <b>huge travel budget</b>?
                    case 0:
                        Id = 44;
                        return false;
                }
                return true;
            case 44:
                // $script:1010151207011615$ 
                // - ...
                // $script:1010151207011616$ 
                // - ...
                switch (selection) {
                    // $script:1010151207011617$
                    // - Say something, $npcName:11004336[gender:1]$.
                    case 0:
                        Id = 45;
                        return false;
                }
                return true;
            case 45:
                // $script:1010174007011620$ 
                // - ...
                return true;
            default:
                return true;
        }
    }
}
