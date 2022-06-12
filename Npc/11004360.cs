using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004360: Aiden
/// </summary>
public class _11004360 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011771$
    // - Is it so much to ask that we have a normal celebration this year?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011772$
                // - I've got a reputation as a know-it-all, but I can't imagine why anyone would do this to our family...
                return 10;
            case (10, 1):
                // $script:1120173007011848$
                // - I rely on science to explain things... but how can it explain <i>this</i>...
                switch (selection) {
                    // $script:1120173007011849$
                    // - You should focus on helping $npcName:11004345[gender:1]$ out here.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1120173007011850$
                // - I'm not so sure about that, honestly.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
