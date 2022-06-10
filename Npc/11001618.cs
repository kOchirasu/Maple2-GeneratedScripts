using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001618: Wei Hong
/// </summary>
public class _11001618 : NpcScript {
    internal _11001618(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516130207006121$ 
                // - What brings you here?
                return true;
            case 10:
                // $script:0531170907006264$ 
                // - You have something to say to me?
                switch (selection) {
                    // $script:0531170907006265$
                    // - The people your thugs took, are they safe?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0531170907006266$ 
                // - Who knows? The poor idiots are probably locked up somewhere. They don't respect the first rule of the streets: you give back as much as you take. Blackstar wants to make 'em pay up their fair share, that's all.
                // $script:0531170907006267$ 
                // - Why do you care, anyway? You friends with one of those vagrants?
                switch (selection) {
                    // $script:0531170907006268$
                    // - Their friends asked me to look into their disappearances.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0531170907006269$ 
                // - Sticking your nose into matters that don't concern you, eh? That's a special kind of stupid. I'd say they better be paying you a fortune, but any friend of those deadbeats wouldn't have two mesos to rub together.
                switch (selection) {
                    // $script:0531170907006270$
                    // - I'm not in this for the money.
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0531170907006271$ 
                // - <font color="#909090">($npc:11001623[gender:0]$ squints at you in disbelief.)</font>
                //   You don't know them and you don't care about getting paid?
                // $script:0531170907006272$ 
                // - You're one of those hero-types. That's fine with me. Go off and get yourself killed. One less idiot to get in my way.
                return true;
            default:
                return true;
        }
    }
}
