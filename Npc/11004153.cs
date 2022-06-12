using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004153: Yentayo
/// </summary>
public class _11004153 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0806025707010577$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0806025707010578$
                // - There are chests hidden all over Maple World, but the ones in $map:02000499$ are... different. Hehe, you'll see!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
