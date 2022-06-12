using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000675: Khan
/// </summary>
public class _11000675 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407002743$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407002744$
                // - Mm? Are you here to challenge me? You can never defeat me, no matter how many times you try. You'd better give up before you get seriously hurt.
                switch (selection) {
                    // $script:0831180407002745$
                    // - I want to challenge you.
                    case 0:
                        return 51;
                    // $script:0831180407002746$
                    // - What's the $map:65000001$?
                    case 1:
                        return 52;
                }
                return -1;
            case (51, 0):
                // $script:0831180407002747$
                // - Heh. Interesting. You challenge the undefeated champion of $map:65000001$, the victor of 47 consecutive matches. Very well. I shall give you what you desire.
                return 51;
            case (51, 1):
                // $script:0831180407002748$
                // - But not right now. We gladiators fight only inside the ring. That's our rule.
                return 51;
            case (51, 2):
                // $script:0831180407002749$
                // - As you can also see, I'm quite busy. Perhaps while I attend to my business, you can start to make a name for yourself. Why not go prove your strength at the $map:65000001$?
                return -1;
            case (52, 0):
                // $script:0831180407002750$
                // - You must not have heard about the $map:65000001$. All right, I shall do you the honor of hearing $npcName:11000675[gender:0]$'s own explanation. So listen.
                return 52;
            case (52, 1):
                // $script:0831180407002751$
                // - The $map:65000001$ is a place of battle where up to 10 warriors can take turns battling one on one, until only one remains. The order of their fights is random.
                return 52;
            case (52, 2):
                // $script:0831180407002752$
                // - Unlucky fighters may be eliminated in their very first match. But those who are truly strong, truly deserving, will triumph over fortune and faith.
                return 52;
            case (52, 3):
                // $script:0831180407002753$
                // - I should know. I've done it countless times. Now... Do you still want to challenge me?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Next,
            (51, 1) => NpcTalkButton.Next,
            (51, 2) => NpcTalkButton.Close,
            (52, 0) => NpcTalkButton.Next,
            (52, 1) => NpcTalkButton.Next,
            (52, 2) => NpcTalkButton.Next,
            (52, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
