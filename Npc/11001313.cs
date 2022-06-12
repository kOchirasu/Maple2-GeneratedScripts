using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001313: Denden
/// </summary>
public class _11001313 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1215203907005032$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1227194507005676$
                // - Yeah? You never see a meerkat before?
                return 40;
            case (40, 1):
                // $script:1227194507005677$
                // - I don't know what you want, but I'm not telling you anything unless <i>you</i> speak, first!
                switch (selection) {
                    // $script:1227194507005678$
                    // - Why does it matter who goes first?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1227194507005679$
                // - It's one of the rules of Meerkat Patrol. So there!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
