using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000361: Marco's Secretary
/// </summary>
public class _11000361 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001499$
    // - How may I help you today?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001501$
                // - $npc:11000065[gender:0]$ is really amazing. When he sets his mind on something, nothing can stop him!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
