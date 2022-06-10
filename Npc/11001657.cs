using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001657: Junta
/// </summary>
public class _11001657 : NpcScript {
    internal _11001657(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0617105607006367$ 
                // - More questions?
                return true;
            case 30:
                // $script:0727223007006865$ 
                // - Halo Mountain...
                switch (selection) {
                    // $script:0727223007006866$
                    // - Is the master really gone?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0727223007006867$
                    // - What do we do now?
                    case 1:
                        Id = 50;
                        return false;
                    // $script:0727223007006868$
                    // - Who was that?
                    case 2:
                        Id = 60;
                        return false;
                }
                return true;
            case 40:
                // $script:0727223007006869$ 
                // - I doubt we've seen the last of him. His command of animus is unlike anything I've ever seen. And until he returns, I will do everything I can to protect Guidance.
                switch (selection) {
                    // $script:0727233607006921$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 50:
                // $script:0727223007006870$ 
                // - I know that we need to evaluate our options carefully... But all I want to do right now is destroy something. I will be deferring to $npcName:11001656[gender:1]$ for now.
                switch (selection) {
                    // $script:0727233607006922$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 60:
                // $script:0727223007006871$ 
                // - I've never seen or heard of him before. Strange that the master never mentioned him, but it sounds like this Kandura lost the title of Munakra to him and has held a grudge ever since.
                // $script:0727223007006872$ 
                // - The power he wields wasn't pure animus. The darkness tainting it was potent.
                switch (selection) {
                    // $script:0727223007006873$
                    // - If I could control my power, I could have...
                    case 0:
                        Id = 61;
                        return false;
                }
                return true;
            case 61:
                // $script:0727223007006874$ 
                // - ...saved him? Perhaps. The animus you possess was honed over centuries of training by one of the greatest masters Guidance had ever known.
                // $script:0727223007006875$ 
                // - And if the master hadn't given you that animus, he may have had the power to stop this. I always feared something like this would happen...
                // $script:0727223007006876$ 
                // - But... I suppose I can no longer humor such thoughts. It is just the three of us now.
                // $script:0727223007006877$ 
                // - Losing him is... I don't...
                // $script:0727223007006878$ 
                // - ...Well, you're his legacy now. Conduct yourself accordingly.
                switch (selection) {
                    // $script:0727223007006879$
                    // - I'll do my best.
                    case 0:
                        Id = 62;
                        return false;
                }
                return true;
            case 62:
                // $script:0727223007006880$ 
                // - Don't misunderstand me. I'm not trying to cheer you up.
                // $script:0727223007006881$ 
                // - I don't like you, and I doubt I ever will. But, like it or not, you are my $male:brother,female:sister$ in Guidance. We must work together if we are to overcome our trials.
                switch (selection) {
                    // $script:0727233607006923$
                    // - Let's talk about something else.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
