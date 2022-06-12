using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001306: Livanda
/// </summary>
public class _11001306 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1215203907005025$
    // - Are you here for my father? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1227194507005647$
                // - Dad's a thoughtful and affection man, if you get to know him.
                return 40;
            case (40, 1):
                // $script:1227194507005648$
                // - There's more to him than he lets on.
                //   <font color="#909090">(There are tears in her eyes.)</font>
                switch (selection) {
                    // $script:1227194507005649$
                    // - Are you okay?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1227194507005650$
                // - I'll be okay...
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
