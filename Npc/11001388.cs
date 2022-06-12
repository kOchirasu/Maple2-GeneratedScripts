using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001388: Chiab
/// </summary>
public class _11001388 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50
    }

    // Select 0:
    // $script:1217193307005388$
    // - This village is good! You just got to look real close to see it.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1223165107005556$
                // - Beautiful day, isn't it? On days like this, I love to pack a lunch and go on a picnic.
                return 40;
            case (40, 1):
                // $script:1223165107005557$
                // - Do you like rainbow trout soup? I cook it with my own blend of spices. Everyone says it's the best soup in town.
                switch (selection) {
                    // $script:1223165107005558$
                    // - <i>I'll</i> be the judge of that!
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1223165107005559$
                // - Ha! All right. Come over to my house sometime, and I'll cook it for you!
                return -1;
            case (50, 0):
                // $script:0201104007005858$
                // - Ah, $MyPCName$. I've got some good news for you. A little while back, $npcName:11001396[gender:1]$ came to see me along with $npcName:11001443[gender:0]$. He asked me to gather the villagers, and then told us about what he'd learned about the people suffering in $map:02010005$. He even brought some materials for us to examine.
                return 50;
            case (50, 1):
                // $script:0201133107005859$
                // - I couldn't understand all the words he used, but I knew what he was trying to say. What they're suffering from is neither a curse nor a disease. $MyPCName$, you were able to come and go without getting sick. So did $npcName:11001443[gender:0]$ and myself. We're the proof of his findings.
                return 50;
            case (50, 2):
                // $script:0201104007005859$
                // - We decided the affected people shouldn't be left in that old hut, though the decision was not agreed to by all. We've moved them to some of our own houses, as well as the doctor's place.
                switch (selection) {
                    // $script:0201104007005860$
                    // - Where are $npcName:11001391[gender:0]$ and $npcName:11001392[gender:1]$?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:0201104007005861$
                // - Ha, don't worry. They're in my house. They're not in the best shape, though. So skinny... must have been tough on them. But with some good food and good sleep, they'll be as good as new in no time. 
                switch (selection) {
                    // $script:0201104007005862$
                    // - That's very kind of you.
                    case 0:
                        return 52;
                }
                return -1;
            case (52, 0):
                // $script:0201104007005863$
                // - Oh, not at all. If anyone's generous here it's you, $MyPCName$. You went out on a limb to help people that you really didn't know. Being so compassionate and talented, you're bound to be successful in whatever you do. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Next,
            (50, 2) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.SelectableDistractor,
            (52, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
