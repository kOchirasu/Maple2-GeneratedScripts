using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000178: Mrs. Ibelin
/// </summary>
public class _11000178 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000734$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000737$
                // - My son is doing very important work at $map:02000001$ Palace. I couldn't provide for him when he was young, but he still grew into such a great man. I'm so proud of him. 
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
