using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004475: Sealon
/// </summary>
public class _11004475 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012161$
    // - You here for the big land grab?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012162$
                // - You here for the big land grab?
                return 10;
            case (10, 1):
                // $script:1227192907012163$
                // - $map:02020041$ is the first city in the new world. This place is gonna be a hotbed of development once we kick the other riffraff off this continent!
                return 10;
            case (10, 2):
                // $script:1227192907012164$
                // - Sure, it seems like a shaky investment <i>now</i>, but just you wait! Any land you buy here today will be worth ten times as much a year from now!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
