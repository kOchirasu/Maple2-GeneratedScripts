using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000119: Frey
/// </summary>
public class _11000119 : NpcScript {
    internal _11000119(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50;70;120
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000508$ 
                // - What brings you here?
                return true;
            case 40:
                // $script:0831180407000512$ 
                // - The Royal Guard protects $npcName:11000075[gender:1]$ and all of $map:02000001$. So long as there are threats to peace in this world, we will not rest.
                return true;
            case 50:
                // $script:0831180407000513$ 
                // - Maybe it's time I told you the truth about why the court was canceled. Just before it was scheduled to start, the leadership met to discuss the details of the proceedings. Suddenly, a bloodied guard stumbled into the meeting and said that the court must be canceled.
                // $script:0831180407000514$ 
                // - We were shocked, as you might imagine. And before we could question him further, a dagger flew in from a nearby window and took his life. There, before our very eyes...
                // $script:0831180407000515$ 
                // - Everyone rushed to find the assailant, but we could find nothing. Our conclusion was that there must be a spy in the palace. The servants of the demon king were plotting something in time for the court. We had to cancel it.
                switch (selection) {
                    // $script:0831180407000516$
                    // - Why didn't you tell anyone what happened?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407000517$ 
                // - You expect us to tell the public that someone was murdered, right in the middle of a meeting like that? People have only just started to calm down after the loss of the Blue Lapenta, we don't need to be riling them back up so soon. 
                return true;
            case 70:
                // $script:1215105107009695$ 
                // - $MyPCName$, what brings you here?
                switch (selection) {
                    // $script:1215105107009696$
                    // - $npcName:11003534$ sent me.
                    case 0:
                        Id = 71;
                        return false;
                }
                return true;
            case 71:
                // $script:1215105107009697$ 
                // - After all this time as the Guard Captain, $npcName:11003534[gender:0]$ still treats me like a child.
                // $script:1215105107009698$ 
                // - You go and tell $npcName:11003534$ that I'll do whatever's necessary to protect $npc:11000075[gender:1]$ and $npcName:11000601[gender:1]$. I swore an oath, and on my life I intend to keep it.
                switch (selection) {
                    // $script:1215105107009699$
                    // - Uh, I'm actually here to ask about the rumors going around $map:02000001$.
                    case 0:
                        Id = 72;
                        return false;
                }
                return true;
            case 72:
                // $script:1215105107009700$ 
                // - Ugh, not you too. These rumors are giving me a headache. I've upped security and tripled patrols to reassure the public, yet the rumors continue to spread.
                switch (selection) {
                    // $script:1215105107009701$
                    // - And what about the truth behind the rumors?
                    case 0:
                        Id = 73;
                        return false;
                }
                return true;
            case 73:
                // $script:1215105107009702$ 
                // - I'll tell you the same thing I told the former captain of the Knights when he stopped by. I don't know anything! If we had any insight into the circumstances behind the rumors, the alliance would be the first to know.
                switch (selection) {
                    // $script:1215105107009703$
                    // - The former captain?
                    case 0:
                        Id = 74;
                        return false;
                }
                return true;
            case 74:
                // $script:1215105107009704$ 
                // - Ah, it's nothing. Don't worry about it.
                switch (selection) {
                    // $script:1215105107009705$
                    // - Okay.
                    case 0:
                        Id = 75;
                        return false;
                }
                return true;
            case 75:
                // $script:1215105107009706$ 
                // - I'm sorry I couldn't be of more help.
                return true;
            case 120:
                // $script:0831180407000518$ 
                // - Some people are curious about my relationship with $npcName:11000076[gender:0]$. It's... quite complicated. I'd rather not get into it.
                return true;
            default:
                return true;
        }
    }
}
