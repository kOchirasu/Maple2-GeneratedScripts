using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004381: Puccini
/// </summary>
public class _11004381 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;40
    }

    // Select 0:
    // $script:1109213607011801$
    // - Why does everyone have to get all lovey-dovey for the holidays? It's gross for the rest of us.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011802$
                // - Why does everyone have to get all lovey-dovey for the holidays? It's gross for the rest of us.
                return -1;
            case (40, 0):
                // $script:1120173007011874$
                // - Why does everyone have to get all lovey-dovey for the holidays? It's gross for the rest of us.
                switch (selection) {
                    // $script:1120173007011875$
                    // - Did you see $npcName:11004345[gender:1]$'s family?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1120173007011876$
                // - I saw $npcName:11004346[gender:0]$ heading for $map:63000073$ early this morning. He goes there every day, you know. He's always got his face stuffed in a book, ignoring his adorable little sister $npcName:11004345[gender:1]$. I'd never let her get bored... So what's his problem?
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
