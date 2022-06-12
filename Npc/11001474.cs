using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001474: Fabid
/// </summary>
public class _11001474 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1224110207005585$
    // - W-what?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1228134707005721$
                // - M-m-must stay calm. I'm n-n-not scared...
                switch (selection) {
                    // $script:0913170607011310$
                    // - What's wrong?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0913170607011311$
                // - <b>AH!!</b> Jeez, you almost gave me a heart attack...
                return 40;
            case (40, 1):
                // $script:0913170607011312$
                // - You aren't headed into the $dungeonTitle:20016002$, are you? I was researching the ruins there when I saw... one of "them!"
                return 40;
            case (40, 2):
                // $script:0913170607011313$
                // - How did the temple of the divine lumarigons come to house such frightening creatures? It's enough to make a man quake in his boots.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
