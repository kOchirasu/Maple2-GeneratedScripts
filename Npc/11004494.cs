using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004494: Pusilla
/// </summary>
public class _11004494 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012354$
    // - This place was a dense forest when we first got here...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012355$
                // - This place was a dense forest when we first got here...
                switch (selection) {
                    // $script:1227192907012356$
                    // - What happened?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012357$
                // - We set up camp just a day after the Daemon Army arrived. This is all that's left of the forest. The stream is totally dead now, too.
                return 11;
            case (11, 1):
                // $script:1227192907012358$
                // - We've seen this kind of rapid transformation before. In the Land of Darkness...
                return 11;
            case (11, 2):
                // $script:1227192907012359$
                // - As the Daemon Army expands, this massive die-off of nature will follow.
                switch (selection) {
                    // $script:0114164507012725$
                    // - That's bad news.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0114164607012725$
                // - We need to stop them before they spread any further.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
