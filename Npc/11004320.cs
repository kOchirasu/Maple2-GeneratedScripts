using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004320: Dunba
/// </summary>
public class _11004320 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    protected override int Select() {
        // Select 0:
        // $script:1102172107011623$
        // - This place is super weird...
        // Select 20:
        // $script:1010140307011449$
        // - This place is super weird...
        // TODO: 0,20
        return 0;
    }

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1102172107011624$
                // - I don't like this place... It's new and scary...
                return -1;
            case (30, 0):
                // $script:1010140307011450$
                // - Ahh! You scared me!
                switch (selection) {
                    // $script:1010140307011451$
                    // - What's gotten into you?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:1010140307011452$
                // - Oh... It's only you. Phew.
                return 40;
            case (40, 1):
                // $script:1010140307011453$
                // - This place has me on edge. Everything's so different.
                return 40;
            case (40, 2):
                // $script:1010140307011454$
                // - It seems like I'm the only one having any trouble fitting in. $npcName:11004322[gender:0]$ is so absorbed in his search for new ingredients. And it seems like $npcName:11004321[gender:1]$ has run out of all patience for me... Sniff.
                return 40;
            case (40, 3):
                // $script:1010140307011455$
                // - I want to be of help tracking down traces of the dragons, but I'm just so anxious. I should've just stayed home.
                switch (selection) {
                    // $script:1010140307011456$
                    // - That's crazy! I'm sure your friends are glad to have you here.
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:1010140307011457$
                // - You really think so? Thanks... That means a lot. I'm sure I can muster up the courage to keep going.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Next,
            (40, 3) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
